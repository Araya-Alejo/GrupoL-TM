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
        MENSAJE_CONSOLA("###########################################################################",visible)
        MENSAJE_CONSOLA("A",visible)
        with open(filename, 'rb') as file:
            MENSAJE_CONSOLA("B",visible)
            binaryData = file.read()
            MENSAJE_CONSOLA("C",visible)
        return binaryData
    except:
        MENSAJE_CONSOLA("D",visible)
        return 0
    finally:
        MENSAJE_CONSOLA("###########################################################################",visible)

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
    path = os.getcwd()
    agregar_usuario(usuario, path + img)

    os.remove(img)
'''
    Procedimiento que captura la imágen
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
