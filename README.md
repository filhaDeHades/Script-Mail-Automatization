# Script for Mail Automatization

READ ME IN PROGRESS...

This script was made for de automatization of e-mails for the [Associação Atlética Acadêmica Ada Lovelace](https://www.facebook.com/piratasdauff).

In the moment, this script sends simple messages e-mails with or without attached PDF documents (working on otimization and refactoring the code)

Leia isso em [Português](https://github.com/filhaDeHades/Script-Mail-Automatization/blob/main/README-pt.md)

## Instructions:
1. **Files organization:**
    The input files must be kept on the "inputs/" folder. The files on that folder must be named by their function:

    - **"inputs.txt":**

    Has strings contain the path for all the input files used and the title for the email.=

    ```
    inputs/login_file.txt
    inputs/recievers.txt
    Título do Email
    inputs/file_simple_message.txt
    inputs/file_html_message.txt
    ```

    - **"sender.txt":**

    Has the login informations for the account that will send the emails.
    Add, in different lines, your email adress and the password of the same email.
    **DO NOT add this file on any repository and/or commit you may do!!**

    ```
    jonh_doe@email.com
    myPassword
    ```

    - **"receiver.txt":**

    Contém a lista de emails para os quais a mensagem deve ser enviada.
    Adicione um email por linha sem espaços adicionais.
    ```
    algum_nome@email.com
    outro_nome@email.com
    ```

    - **"message.txt":**

    Contém a mensagem do corpo do email em forma de texto simples.
    Escreva a mensagem da forma como você espera que ela seja apresentada.

    - **"index.html":**

    Contém a mensagem do corpo do email em HTML.


2. **Configurações adicionais:**
    - Ativar login por app menos seguro

3. **Para enviar emails simples:**

4. **Para enviar emails com anexo:**

5. **Para enviar emails HTML:**
    O arquivo "inputs.txt" deve conter 5 informações diferentes, sendo elas: arquivo de login, arquivo de destinatários, título do email, arquivo de mensagem simples e arquivo html.

## Functions:

2. **sendEmail(loginFile, toFile, title, messageFile):**
Recieve files with login data, e-mail adresses and the message to be send, as so the title of the message.

    - **loginFile**: File with the login data.

    - **toFile**: File with the e-mail adresses.

    - **title**: Title of the message to be send.

    - **messageFile**: File with the message to be send.


3. **collectEmails(emailFile):**
Take the file with the e-mail adresses and **return a list**.

    - **emailFile**: File with the e-mail adresses.


4. **takeMessage(messageFile):**
Take the file with the message to be send and **return a list with de content**.

    - **messageFile**: File with the message to be send.

5. **loginData(loginFile):**
Take the file with login data and **return a list with the content**.

    - **loginFile**: File with the login data.