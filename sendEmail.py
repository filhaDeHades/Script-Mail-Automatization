from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import close
import smtplib
from unidecode import unidecode

def sendEmail(loginFile, toFile, title, messageFile):
    loginList = collectData(loginFile, 0)
    toList = collectData(toFile, 1)
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
    

def sendEmailWithAttachments(loginFile, to, title, message, attachFileName):
    loginList = collectData(loginFile, 0)

    try:
        # logFile = open('log-envio-de-emails.txt', 'a', encoding='utf-8')
        # logFile.write(f'\nPARA: {to}\nTÍTULO: {title}\nARQUIVO A SER ANEXADO: {attachFileName}\n')
        # logFile.close()
        pass
    except:
        print('ERRO ao manipular arquivo de log')
        close(1)

    try:
        msg = MIMEMultipart()

        msg['From'] = loginList[0]
        msg['Subject'] = title

        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        fileName = open(attachFileName, 'rb')
        content = fileName.read()

        part = MIMEBase('application', "octet-stream")
        part.set_payload(content)
        encoders.encode_base64(part)

        nomeArquivo = attachFileName.split('\\')

        part.add_header('Content-Disposition', f'attachment; filename={nomeArquivo[-1]}')

        msg.attach(part)

        fileName.close()

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(msg['From'], loginList[1])

        msg['To'] = to
        server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

        server.quit()

        print("successfully sent email with attachments")
    except:
        print("Erro ao ENVIAR o email com anexo.")
        close(1)


def sendManyEmails(loginFile, toFile, title, messageFile, namesFile, attachFile):
    toList = collectData(toFile, 1)
    message = ''
    namesList = collectData(namesFile, 2)

    pathCert = input('Digite o caminho até o certificado (colocar barras como "\\\\") e o texto-base:\n')
    attachList = collectData(attachFile, 3, pathCert, '.pdf')

    try:
        if(len(toList) == len(namesList) == len(attachList)):
            for i in range(len(toList)):
                print(f'Enviando email {i}...')
                inicio = f'Olá {namesList[i]},\n\n'
                message = inicio + takeMessage(messageFile)

                sendEmailWithAttachments(loginFile, toList[i], title, message, attachList[i])

            pass
        else:
            print('ERRO diferença de número de emails, número de nomes e anexos.')
            close(1)
    except:
        print('ERRO. Falha ao enviar muitos emails.')


    pass


def collectData(dataFile, dataType, prefix='', sufix=''):
    dataList = []

    try:
        file = open(dataFile, 'r', encoding='utf-8')

        for data in file:
            data = data.strip('\n')
            if(dataType == 3):
                data = data.title()
                data = data.replace(' ', '')
                data = unidecode(data)
            data = prefix + data + sufix
            dataList.append(data)

        file.close()
        return dataList
    except:
        if(dataType == 0):
            print('Erro ao ler o arquivo de LOGIN.')
        elif (dataType == 1):
            print('Erro ao ler o arquivo de EMAILS.')
        elif (dataType == 2):
            print('Erro ao ler o arquivo de NOMES.')
        elif (dataType == 3):
            print('Erro ao ler o arquivo de ANEXOS.')
        close(1)


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


def readInput(inputFile):
    inputData = []
    
    try:
        file = open(inputFile, 'r', encoding='utf-8')
        for line in file:
            line = line.strip('\n')
            inputData.append(line)
        file.close()
        if len(inputData) == 4 or len(inputData) == 6:
            return inputData
        else:
            print('Erro ao ler o arquivo de INPUT. Quantidade de dados incorreta no arquivo.')
            return None
    except:
        print('Erro ao ler o arquivo de INPUT.')
        return None


inputFile = input('Digite o caminho para o arquivo de inputs: ')
inputData = readInput(inputFile)

if len(inputData) == 4:
    sendEmail(inputData[0], inputData[1], inputData[2], inputData[3])
elif len(inputData) == 6:
    sendManyEmails(inputData[0], inputData[1], inputData[2], inputData[3], inputData[4], inputData[5])