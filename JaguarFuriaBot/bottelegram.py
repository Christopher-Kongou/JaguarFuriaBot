import telebot

chave_api = "7507846177:AAEMKoztkw_5LUQ9ZFfitSzc9unX-1Qokts"

bot = telebot.TeleBot(chave_api)


@bot.message_handler(commands=["lojafuria"])
def lojafuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "https://www.furia.gg/")


@bot.message_handler(commands=["instagramfuria"])
def instagramfuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "https://www.instagram.com/furiagg/")


@bot.message_handler(commands=["xfuria"])
def xfuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "https://x.com/FURIA")


@bot.message_handler(commands=["csfuria"])
def csfuria(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id,
                     "https://liquipedia.net/counterstrike/FURIA")


def verificar(mensagem):
    return True


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


bot.polling()
