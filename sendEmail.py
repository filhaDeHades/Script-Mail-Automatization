from email.message import EmailMessage
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


def sendHTMLEmail(loginFile, to, title, message, htmlFile):
    """Send HTML Emails to the adresses on the 'to' file.

    Args:
        loginFile (str): Name of the file with the login data.
        to (str): Name of the file contain the list of receivers for the email.
        title (str): Title of the email.
        message (str): Name of the file contain the simples text message for the body of the email.
        htmlFile (str): Name of the HTML file contain the stylized message for the body of the email.
    """
    
    loginList = collectData(loginFile, 0)
    toList = collectData(to, 1)
    message = takeMessage(message)
    html = takeMessage(htmlFile)

    try:
        for i in toList:
            msg = EmailMessage()

            msg['From'] = loginList[0]
            msg['Subject'] = title

            msg.attach(MIMEText(message, 'plain', 'utf-8'))
            msg.set_content(message)
            msg.add_alternative(html, subtype='html')

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.ehlo()
            server.starttls()
            server.ehlo()


            server.login(msg['From'], loginList[1])

        
            msg['To'] = i
            server.send_message(msg)

            server.quit()

            print("successfully sent HTML email")
    except:
        print("Erro ao ENVIAR o email HTML.")


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



def collectData(dataFile, dataType, prefix='', sufix=''):
    """Collect the data from one of the input files.

    Args:
        dataFile (str): Name of the file scanned.
        dataType (int): Indicates what type of input file it is.
        prefix (str, optional): Used for attachment files. Defaults to ''.
        sufix (str, optional): Used for attachment files. Defaults to ''.

    Returns:
        _type_: _description_
    """

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
        if len(inputData) >= 4 and len(inputData) <= 6:
            return inputData
        else:
            print('Erro ao ler o arquivo de INPUT. Quantidade de dados incorreta no arquivo.')
            return None
    except:
        print('Erro ao ler o arquivo de INPUT.')
        return None


if __name__ == "__main__":

    #inputFile = input('Digite o caminho para o arquivo de inputs: ')
    inputFile = "inputs/inputs.txt"
    inputData = readInput(inputFile)

    if len(inputData) == 4:
        sendEmail(inputData[0], inputData[1], inputData[2], inputData[3])
    elif len(inputData) == 5:
        sendHTMLEmail(inputData[0], inputData[1], inputData[2], inputData[3], inputData[4])
    elif len(inputData) == 6:
        sendManyEmails(inputData[0], inputData[1], inputData[2], inputData[3], inputData[4], inputData[5])