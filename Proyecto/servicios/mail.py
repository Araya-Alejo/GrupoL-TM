'''
    Conexion con la platadorma de Gmail y envio de mail
    @author Araya
'''
# ------------------------------------------------------------------------------
import smtplib
import servicios.SO
from interfaces.ESTANDARES import *
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from smtplib import SMTP


def ENVIAR_CORREO(MAIL_OTHER_USER):
    try:
        conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)
        conexion.ehlo()

        conexion.starttls()
        #MENSAJE_CONSOLA("Conexion con mail ok", visible)
        conexion.login(user= "documentacion.facultad@gmail.com", password = "orcv kddq gahc dsbr")
        #MENSAJE_CONSOLA("autenticacion ok", visible)
        #mensaje= "Subject: AlquilaYaPrueba\nSaludos Sr/Sra:"
        #mensaje = "Subject: AlquilaYaPrueba2\n"+palabra
        #mensaje = "Subject: AlquilaYaPrueba3\nAlquiler"
        mensaje = "Subject: AlquilaYa\nLa operacion se ha realizado con exito, muchas gracias por trabajar con nosotros."
        conexion.sendmail(from_addr= "documentacion.facultad@gmail.com", to_addrs=MAIL_OTHER_USER,msg= mensaje)
    except Exception:
        MENSAJE_CONSOLA(str(Exception), visible)
    finally:
        conexion.quit()





"""
def enviarMail(mensaje, emailReceptor)
    mensaje = MIMEMultipart("plain")
    mensaje["From"]="alquilaya.utn@outlook.com"
    mensaje["To"]= "rxvargas.92@gmail.com"
    mensaje["Subject"] ="Correo de prueba desde Python 3"
    adjunto = MIMEBase("application","octect-stream")
    adjunto.set_payload(open("yourDocument.txt","rb").read())
    adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
    mensaje.attach(adjunto)
    smtp = SMTP("smtp.live.com")
    #smtp.gmail.com for google accounts
    #smtp.yahoo.com for yahoo accounts
    smtp.starttls()
    smtp.login("yourMail","yourPassword")
    smtp.sendmail("yourMail","targetMail",mensaje.as_string())
    smtp.quit()
"""
