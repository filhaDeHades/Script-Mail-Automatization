# Script for Mail Automatization

This script was made for de automatization of e-mails.
In the moment, this script only send simple messages e-mails with or without attached PDF documents.

## Instructions:
1. **Files organization:**
    - **Login Data:**
    Add your e-mail and password, in this order, on different lines.

    - **e-Mails:**
    Add one e-mail for line, without adicional spaces.

    - **Message:**
    Write the message in the way you want it to show.

    - **Files:**
    Files that will be sent on the e-mails.

## Functions:

2. **sendEmail(loginFile, toFile, title, messageFile):**
Recieve files with login data, e-mail adresses and the message to be send, as so the title of the message.

    - **loginFile**: File with the login data.

    - **toFile**: File with the e-mail adresses.

    - **title**: Title of the message to be send.

    - **messageFile**: File with the message to be send.


3. **collectEmails(emailFile):**
Take the file with the e-mail adresses and **retorn a list**.

    - **emailFile**: File with the e-mail adresses.


4. **takeMessage(messageFile):**
Take the file with the message to be send and **retorn a list with de content**.

    - **messageFile**: File with the message to be send.

5. **loginData(loginFile):**
Take the file with login data and **retorn a list with the content**.

    - **loginFile**: File with the login data.