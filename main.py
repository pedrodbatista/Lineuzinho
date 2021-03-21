from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random

API_TOKEN = "1700885261:AAETCokNpqNDk44x3d5XASfnQfzxiNOKWfI"

CONTATINHOS_SHEET_LINK = "https://docs.google.com/spreadsheets/d/1Kfy-tCDA_UggPUOaYs1w9oN_DtuL6GBWPyCmcl_R3f8/edit?usp=sharing"
GITHUB_REPO_LINK = "https://github.com/lineuzinho-icmc/lineuzinho"
SAVED_DOCS_LINK = "https://t.me/docs21"

DOCS_CHANNEL_MESSAGES_MAX = 800

def start(update, context):
    update.message.reply_text("pó fala meu rei")

def contatinhos(update, context):
    update.message.reply_text("CHAMA NOS CONTATINHO")
    update.message.reply_text(CONTATINHOS_SHEET_LINK, disable_web_page_preview=True)

def help(update, context):
    update.message.reply_text(GITHUB_REPO_LINK)

def save(update, context):
    originalMessage = update.message.reply_to_message
    if not originalMessage or not originalMessage.text:
        update.message.reply_text("faz o comando respondendo alguma coisa...", parse_mode="Markdown")

    context.bot.forwardMessage("@docs21", update.effective_chat.id, originalMessage.message_id)

def docsChannel(update, context):
    update.message.reply_text(SAVED_DOCS_LINK)

def newMembersGreetings(update, context):
    newMembers = update.message.new_chat_members
    welcomeVocative = ""
    if len(newMembers) > 1:
        for newMember in newMembers[:-1]:
            welcomeVocative += "{0}, ".format(newMember.first_name.split(" ")[0].capitalize())
        welcomeVocative += " e {0}".format(newMembers[-1].first_name.split(" ")[0].capitalize())
    else:
        welcomeVocative = newMembers[0].first_name.split(" ")[0].capitalize()
    
    update.message.reply_text("Boas vindas, {0} rsrs".format(welcomeVocative))

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO
    )

    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("save", save))
    dp.add_handler(CommandHandler("docs", docsChannel))
    dp.add_handler(CommandHandler("contatinhos", contatinhos))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newMembersGreetings))

    updater.start_polling()
    logging.info("=== Lineuzinho up&running! ===")
    updater.idle()
    logging.info("=== Lineuzinho shutting down :( ===")

if __name__ == "__main__":
    main()