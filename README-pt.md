# Script para Envio de Emails

Esse script foi criado para automatizar o envio de emails para a [Associação Atlética Acadêmica Ada Lovelace](https://www.facebook.com/piratasdauff).

Atualmente o script envia emails de mensagens simples e com anexos do tipo PDF (ainda em desenvolvimento pra otimização) e emails HTML.

Read this in [English](https://github.com/filhaDeHades/Script-Mail-Automatization/blob/main/README.md)

## Instruções:
1. **Organização dos Arquivos:**
    Os arquivos de input devem ser adicionados na pasta "inputs". Os arquivos nessa pasta devem ser nomeados conforme sua função:

    - **"inputs.txt":**

    Contém o nome de todos os caminhos para os arquivos utilizados pelo script (organizados de acordo com sua função) e o título do email.

    ```
    arquivo_de_login.txt
    arquivo_dos_destinatários.txt
    Título do Email
    arquivo_mensagem_simples.txt
    arquivo_mensagem_html.txt
    ```

    - **"sender.txt":**

    Contém as informações de login para envio do email.
    Adicione o email do qual a mensagem deve ser enviada e a senha desse mesmo email, respectivamente, em linhas separadas.
    **NÃO adicione esse arquivo a nenhum repositório e/ou commit que você possa criar!!**

    ```
    jose_dos_santos@email.com
    minhaSenha
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

    - **Arquivos:**

    ~Arquivos que serão enviados pelos emails. (no momento só arquivos PDF).~

2. **Configurações adicionais:**
    - Ativar login por app menos seguro

3. **Para enviar emails simples:**

4. **Para enviar emails com anexo:**

5. **Para enviar emails HTML:**
    O arquivo "inputs.txt" deve conter 5 informações diferentes, sendo elas: arquivo de login, arquivo de destinatários, título do email, arquivo de mensagem simples e arquivo html.

## Funções:

1. **sendEmail(loginFile, toFile, title, messageFile):**
Recebe arquivos contendo informações de login,  endereços de email que receberam a mensagem e a mensagem a ser enviada, além do título da mensagem e envia o email.

    - **loginFile**: Arquivo contendo as informações de login.

    - **toFile**: Arquivo contendo os emails que receberam a mensagem.

    - **title**: Título da mensagem a ser enviada.

    - **messageFile**: Arquivo contendo a mensagem a ser enviada.


2. **sendEmailWithAttachments(loginFile, to, title, message, attachFileName):**
Envia uma mensagem com um anexo para apenas um email.

    - **loginFile**: Caminho para o arquivo de login.

    - **to**: Email para o qual a mensagem será enviada.

    - **title**: Título do email.

    - **message**: Mensagem que será enviada no email.

    - **attachFileName**: Nome do arquivo a ser anexado.


3. **sendManyEmails(loginFile, toFile, title, messageFile, namesFile, attachFile):**
Envia vários emails de uma vez para uma lista de endereços.

    - **loginFile**: Caminho para o arquivo de login.

    - **toFile**: Caminho para o arquivo de emails que receberam a mensagem.

    - **title**: Título do email.

    - **messageFile**: Caminho para o arquivo contendo o corpo da mensagem.

    - **namesFile**: Arquivo com o nome das pessoas que receberam os emails.

    - **attachFile**: Arquivo contendo os nomes das pessoas que receberam os certificados.

4. **takeMessage(messageFile):**
Pega o arquivo contendo a mensagem a ser enviada e **retorna uma lista com o conteúdo**.

    - **messageFile**: Arquivo contendo a mensagem a ser enviada.

5. **readInput(inputFile):**
Lê o input do usuário.

    - **inputFile**: Arquivo contendo as informações de input.