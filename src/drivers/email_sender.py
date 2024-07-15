import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_addrs, body):
    from_addr = 'v57srilrst5weydc@ethereal.email'
    login = 'v57srilrst5weydc@ethereal.email'
    password = 'HV9cN56nekd6CU7HQj'

    msg = MIMEMultipart()
    msg['From'] = "viagens_confirma@email.com"
    msg['To'] = ', '.join(to_addrs)

    msg['Subject'] = "Confirmação de viagem"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.ethereal.email', 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()