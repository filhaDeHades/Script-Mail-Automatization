# Script para Envio de Emails

Esse script foi criado para automatizar o envio de emails Para a [Associação Atlética Acadêmica Ada Lovelace](https://www.facebook.com/piratasdauff).

Atualmente o script envia envia emails de mensagens simples e com anexos do tipo PDF.

## Instruções:
1. **Organização dos Arquivos:**
    - **Dados de Login:**
    Adicione o email do qual a mensagem deve ser enviada e a senha desse mesmo email, respectivamente, em linhas diferentes.

    - **Emails de Destino:**
    Adicione um email por linha sem espaços adicionais.

    - **Mensagem:**
    Escreva a mensagem da forma como você espera que ela seja apresentada.

    - **Arquivos:**
    Arquivos que serão enviados pelos emails. (no momento só arquivos PDF).

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

4. **collectData(dataFile, dataType, prefix='', sufix=''):**
Coleta os dados dos arquivos.

    - **dataFile**: Arquivo cujas informações devem ser retiradas.

    - **dataType**: Tipo do arquivo que será aberto.

    - **prefix**: Início do nome dos arquivos.

    - **sufix**: Fim do nome dos arquivos.

5. **takeMessage(messageFile):**
Pega o arquivo contendo a mensagem a ser enviada e **retorna uma lista com o conteúdo**.

    - **messageFile**: Arquivo contendo a mensagem a ser enviada.

6. **readInput(inputFile):**
Lê o input do usuário.

    - **inputFile**: Arquivo contendo as informações de input.