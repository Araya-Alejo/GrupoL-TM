import smtplib
import SO

conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)
conexion.ehlo()

conexion.starttls()

conexion.login(user= SO.MAIL_USER, password = SO.MAIL_PASSWORD)

mensaje = "Subject: AlquilaYa\nEste es la factura del auto, muchas gracias por trabajar con nosotros."
conexion.sendmail(from_addr= SO.MAIL_USER, to_addrs=SO.MAIL_USER,msg= mensaje)

conexion.quit()
