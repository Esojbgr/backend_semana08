from smtplib import SMTP
from email.message import EmailMessage
from os import getenv


def enviar_correo(destinatarios, asunto, cuerpo):
    mensaje = EmailMessage()
    # Primero configuramos el emisor y este emisor tiene que ser el mismo que el de las credenciales
    mensaje["From"] = getenv("EMAIL")

    # A quién voy a enviar el correo
    mensaje["To"] = destinatarios

    # Título del correo
    mensaje["Subject"] = asunto

    # Contenido del correo
    mensaje.set_content(cuerpo)
    mensaje.add_alternative(cuerpo, subtype='html')

    servidor = SMTP(host=getenv("SMTP_HOST"), port=getenv("SMTP_PORT"))

    # Inicializa la conexión con mi servidor de correo
    servidor.starttls()

    # Nos autenticamos en el servidor de correos
    servidor.login(user=getenv("EMAIL"), password=getenv("EMAIL_PASSWORD"))

    # Enviamos el correo
    servidor.send_message(mensaje)

    # Cerramos la conexión con el servidor de correo
    servidor.close()
