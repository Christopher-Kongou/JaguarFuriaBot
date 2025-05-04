LEIA ME
🧾 Sumário
1 Descrição Geral
2 Dependências
3 Configuração Inicial
4 Funcionamento do Bot
5 Manipuladores de Comandos
6 Função de Verificação e Resposta Padrão
7 Execução do Bot

1.📝 Descrição Geral
Este script implementa um bot para o Telegram que responde a comandos específicos relacionados à Equipe de eSports FURIA. Quando um usuário envia determinados comandos, o bot responde com links úteis como o site da loja oficial, Instagram, Twitter/X, e página da equipe de CS na Liquipedia.

O bot está sempre ouvindo (através do polling) e fornece uma mensagem padrão para ajudar o usuário a escolher uma das opções disponíveis.

2.📦 Dependências
Python 3.6+

Biblioteca telebot (pyTelegramBotAPI)

Instalação da Biblioteca:
pip install pyTelegramBotAPI

3.⚙️ Configuração Inicial
import telebot

chave_api = "API"
bot = telebot.TeleBot(chave_api)
chave_api: substitua "API" por sua chave de API oficial do BotFather no Telegram.

telebot.TeleBot(chave_api): inicializa a instância do bot com a chave fornecida.

4.🤖 Funcionamento do Bot
O bot responde a comandos específicos enviados por usuários no chat do Telegram. Cada comando é registrado por um "handler" que escuta e responde quando o comando é digitado.

5.🧭 Manipuladores de Comandos
1. /lojafuria
@bot.message_handler(commands=["lojafuria"])
def lojafuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "https://www.furia.gg/")
Envia o link para a loja oficial da FURIA.

mensagem.chat.id: identifica o chat do usuário para enviar a resposta.

2. /instagramfuria
@bot.message_handler(commands=["instagramfuria"])
def instagramfuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "https://www.instagram.com/furiagg/")
Envia o link para o Instagram oficial da FURIA.

3. /xfuria
@bot.message_handler(commands=["xfuria"])
def xfuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "https://x.com/FURIA")
Envia o link para o perfil oficial da FURIA no X (antigo Twitter).

4. /csfuria
@bot.message_handler(commands=["csfuria"])
def csfuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id,
                     "https://liquipedia.net/counterstrike/FURIA")
Fornece um link para a página da equipe de CS:GO da FURIA na Liquipedia.

6.🧠 Função de Verificação e Resposta Padrão
Função de Verificação:
def verificar(mensagem):
    return True
Essa função sempre retorna True, o que faz com que todas as mensagens que não são comandos específicos sejam tratadas pelo próximo handler.

Resposta Padrão:
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item)
/lojafuria                 Loja da Furia
/instagramfuria     Instagram da Furia
/xfuria                     X da Furia
/csfuria                   Tudo sobre o Counter Strike da Furia
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)
Caso o usuário envie qualquer texto que não seja um comando reconhecido, o bot responde com uma mensagem de menu oferecendo as opções de comando clicáveis.

7.▶️ Execução do Bot
bot.polling()
polling() inicia o loop principal do bot, onde ele fica escutando mensagens em tempo real.

Isso mantém o bot ativo e pronto para responder comandos e mensagens.
