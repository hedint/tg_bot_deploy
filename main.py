import logging
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.effective_message.reply_text("Hi!")


def echo(update, context):
    update.effective_message.reply_text(update.effective_message.text)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1752966025:AAH4HsOL_7g7xRb8efZTeDNKBp6LyeT0fx4"
    NAME = "tg-test-bot-volodin"

    # Port is given by Heroku
    PORT = os.environ.get('PORT', 80)

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=f"https://{NAME}.herokuapp.com/{TOKEN}")
    logger.error(f"https://{NAME}.herokuapp.com/{TOKEN}")
    logger.error(f"https://{NAME}.herokuapp.com/{PORT}")

    updater.idle()