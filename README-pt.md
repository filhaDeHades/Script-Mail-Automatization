# Script para Envio de Emails

Esse script foi criado para automatizar o envio de emails.
Atualmente o script só envia emails de mensagens simples.

## Instruções:
1. **Organização dos Arquivos:**
    - **Dados de Login:**
    Adicione o email do qual a mensagem deve ser enviada e a senha desse mesmo email, respectivamente, em linhas diferentes.

    - **Emails:**
    Adicione um email por linha sem espaços adicionais.

    - **Mensagem:**
    Escreva a mensagem da forma como você espera que ela seja apresentada.

## Funções:

1. **sendEmail(loginFile, toFile, title, messageFile):**
Recebe arquivos contendo informações de login,  endereços de email que receberam a mensagem e a mensagem a ser enviada, além do título da mensagem e envia o email.

    - **loginFile**: Arquivo contendo as informações de login.

    - **toFile**: Arquivo contendo os emails que receberam a mensagem.

    - **title**: Título da mensagem a ser enviada.

    - **messageFile**: Arquivo contendo a mensagem a ser enviada.


2. **collectEmails(emailFile):**
Pega o arquivo contendo os contatos para os quais a mensagem deve ser enviada e **retorna uma lista**.

    - **emailFile**: Arquivo contendo os emails que receberam a mensagem.


3. **takeMessage(messageFile):**
Pega o arquivo contendo a mensagem a ser enviada e **retorna uma lista com o conteúdo**.

    - **messageFile**: Arquivo contendo a mensagem a ser enviada.

4. **loginData(loginFile):**
Pega o arquivo contendo os dados de login e **retorna uma lista com o conteúdo**.

    - **loginFile**: Arquivo contendo as informações de login.