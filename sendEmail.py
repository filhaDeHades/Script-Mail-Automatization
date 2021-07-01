from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendEmail(loginFile, toFile, title, messageFile):
    loginList = loginData(loginFile)
    toList = collectEmails(toFile)
    message = takeMessage(messageFile)

    try:
        msg = MIMEMultipart()

        msg['From'] = loginList[0]
        msg['Subject'] = title

        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.ehlo()
        server.starttls()
        server.ehlo()


        server.login(msg['From'], loginList[1])

        for i in toList:
            msg['To'] = i
            server.sendmail(msg['From'], i, msg.as_string())

        server.quit()

        print("successfully sent email")
    except:
        print("Erro ao ENVIAR o email.")
    

def collectEmails(emailFile):
    receiver = []

    try:
        file = open(emailFile, 'r')

        for email in file:
            email= email.strip('\n')
            receiver.append(email)

        file.close()
        return receiver
    except:
        print('Erro ao ler o arquivo de EMAILS.')
    

def takeMessage(messageFile):
    message = ''

    try:
        file = open(messageFile, 'r')

        for line in file:
            message += line

        file.close()
        return message
    except:
        print('Erro ao ler o arquivo de MENSAGEM.')


def loginData(loginFile):
    login = []

    try:
        file = open(loginFile)
        for line in file:
            line = line.strip('\n')
            login.append(line)
        file.close()
        return login
    except:
        print('Erro ao ler o arquivo de LOGIN.')
    


sendEmail('login/dadosDeLogin.txt', 'listasDeEmail/testeEmails.txt', 'Oi mamiz, Como vai?', 'mensagensDeEmail/testeMensagem.txt')