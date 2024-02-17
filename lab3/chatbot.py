import telegram
from telegram.ext import Updater, MessageHandler, Filters
import configparser
import logging


def main():
    # Load your token and create an Updater for your Bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=config['TELEGRAM']['ACCESS_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher

    # Set up logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Register a dispatcher to handle message
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()


def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("Context: " + str(context))
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
