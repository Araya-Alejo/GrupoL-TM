# pip install opencv-python
# pip install matplotlib
# pip install mtcnn
# pip install tensorflow
# ------------------------------------------------------------------------------
import os
import cv2
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
from entidades.usuario import Usuario
from servicios.usuarioservicios_basedatos import agregar_usuario
from interfaces.ESTANDARES import *
# ------------------------------------------------------------------------------
'''
    Función que convierte una imágen a formato binario.
'''
def convertToBinaryData(filename):
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

# ------------------------------------------------------------------------------
    #REGISTRO
# ------------------------------------------------------------------------------
'''
    Procedimiento que detecta el rostro de la imágen.
'''
def face(img, faces):
    data = plt.imread(img)
    for i in range(len(faces)):
        x1, y1, ancho, alto = faces[i]["box"]
        x2, y2 = x1 + ancho, y1 + alto
        plt.subplot(1,len(faces), i + 1)
        plt.axis("off")
        face = cv2.resize(data[y1:y2, x1:x2],(150,200), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(img, face)
        plt.imshow(data[y1:y2, x1:x2])

'''
    Procedimiento que llama al método para cargar el usuario a la base de datos.
    Envía un Usuario y la imágen (ya convertida en binario).
'''
def register_face_db(usuario, img):
    path = os.getcwd().replace("\\", "/") + "/"
    agregar_usuario(usuario, path + img)

    os.remove(img)
'''
    Procedimiento que captura la imágen de registro.
'''
def register_capture(usuario):
    cap = cv2.VideoCapture(0)
    user_reg_img = usuario.getCuil()                                            # Nombre de la imagen (Número de cuil)
    img = f"{user_reg_img}.jpg"                                                 # Al nombre de la imagen se agrega .jpg

    while True:                                                                 # Bucle que se ejecutará hasta que se capture la imagen (Tecla Esc)
        ret, frame = cap.read()
        cv2.imshow("Registro Facial", frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    pixels = plt.imread(img)
    faces = MTCNN().detect_faces(pixels)
    face(img, faces)
    register_face_db(usuario, img)

# ------------------------------------------------------------------------------
    #LOGIN
# ------------------------------------------------------------------------------
'''
    Función para compatibilidad entre imágenes
'''
def compatibility(img1, img2):
    orb = cv2.ORB_create()

    kpa, dac1 = orb.detectAndCompute(img1, None)
    kpa, dac2 = orb.detectAndCompute(img2, None)

    comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = comp.match(dac1, dac2)

    similar = [x for x in matches if x.distance < 70]
    if len(matches) == 0:
        return 0
    return len(similar)/len(matches)

'''
    Procedimiento para capturar imágen de login
'''
def login_capture(cuil):
    cap = cv2.VideoCapture(0)
    user_login = cuil
    img = f"{user_login}_login.jpg"
    img_user = f"{user_login}.jpg"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Login Facial", frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    pixels = plt.imread(img)
    faces = MTCNN().detect_faces(pixels)

    face(img, faces)

    path = os.getcwd().replace("\\", "/") + "/"
    res_db = db.getUser(user_login, path + img_user)
    if(red_db != None):
        my_files = os.listdir()
        if (img_user in my_files):
            face_reg = cv2.imread(img_user, 0)
            face_log = cv2.imread(img, 0)

            comp = compatibility(face_reg, face_log)

            if (comp >= 0.94):
                #print("{}Compatibilidad del {:.1%}{}".format(color_success, float(comp), color_normal))
                print("Bienvenido")
            else:
                #print("{}Compatibilidad del {:.1%}{}".format(color_error, float(comp), color_normal))
                print("No es Bienvenido")
            os.remove(img_user)

        else:
            print("¡Error! Usuario no encontrado")
    else:
        print("¡Error! Usuario no encontrado")
    os.remove(img)
