import smtplib
import servicios.SO
import interfaces.ESTANDARES

def ENVIAR_CORREO(mensaje, MAIL_OTHER_USER):
    try:
        conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)
        conexion.ehlo()

        conexion.starttls()

        conexion.login(user= SO.MAIL_USER, password = SO.MAIL_PASSWORD)
        #mensaje = "Subject: AlquilaYa\nEste es la factura del auto, muchas gracias por trabajar con nosotros."
        conexion.sendmail(from_addr= SO.MAIL_USER, to_addrs=MAIL_OTHER_USER,msg= mensaje)
    except Exception:
        MENSAJE_CONSOLA("Mail no valido", visible)
    finally:
        conexion.quit()
