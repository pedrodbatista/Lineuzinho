from telegram.ext import Updater, CommandHandler
import logging

API_TOKEN = "1700885261:AAETCokNpqNDk44x3d5XASfnQfzxiNOKWfI"
CONTATINHOS_SHEET_LINK = "https://docs.google.com/spreadsheets/d/1Kfy-tCDA_UggPUOaYs1w9oN_DtuL6GBWPyCmcl_R3f8/edit?usp=sharing"

def start(update, context):
    s = "pó fala meu rei"
    update.message.reply_text(s)

def contatinhos(update, context):
    update.message.reply_text("CHAMA NO CONTATINHO")
    update.message.reply_text(CONTATINHOS_SHEET_LINK)

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO
    )

    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("contatinhos", contatinhos))

    updater.start_polling()
    logging.info("=== Bot running! ===")
    updater.idle()
    logging.info("=== Bot shutting down! ===")

if __name__ == "__main__":
    main()