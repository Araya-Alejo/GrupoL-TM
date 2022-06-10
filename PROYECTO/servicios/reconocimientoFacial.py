# pip install opencv-python
# pip install matplotlib
# pip install mtcnn
# pip install tensorflow
# ------------------------------------------------------------------------------
import os
import cv2
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
# ------------------------------------------------------------------------------
'''
'''
def convertToBinaryData(filename):
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

'''
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
'''
def register_face_db(usuario, img):
    # Tendrias que llamar a la funcion para ingresar el usario a la db
    # Le envias el usario y la imagen
    # imgNombre = img.replace(".jpg", "").replace(".png", "")

    os.remove(img)

'''
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
