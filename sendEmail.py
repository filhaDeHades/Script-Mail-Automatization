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
            server.sendmail(msg['From'], i, msg.as_string().encode('utf-8'))

        server.quit()

        print("successfully sent email")
    except:
        print("Erro ao ENVIAR o email.")
    

def collectEmails(emailFile):
    receiver = []

    try:
        file = open(emailFile, 'r', encoding='utf-8')

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
        file = open(messageFile, 'r', encoding='utf-8')

        for line in file:
            message += line

        file.close()
        return message
    except:
        print('Erro ao ler o arquivo de MENSAGEM.')


def loginData(loginFile):
    login = []

    try:
        file = open(loginFile, 'r', encoding='utf-8')
        for line in file:
            line = line.strip('\n')
            login.append(line)
        file.close()
        return login
    except:
        print('Erro ao ler o arquivo de LOGIN.')
    

def readInput(inputFile):
    inputData = []
    
    try:
        file = open(inputFile, 'r', encoding='utf-8')
        for line in file:
            line = line.strip('\n')
            inputData.append(line)
        file.close()
        if len(inputData) == 4:
            return inputData
        else:
            print('Erro ao ler o arquivo de INPUT. Quantidade de dados incorreta no arquivo.')
            return None
    except:
        print('Erro ao ler o arquivo de INPUT.')
        return None


inputFile = input('Digite o nome do arquivo de inputs: ')
inputData = readInput(inputFile)

sendEmail(inputData[0], inputData[1], inputData[2], inputData[3])