from telegram.ext import Updater, MessageHandler, Filters
from bot_tokens import BOT_TOKEN


def echo(upd, ctx):
    upd.message.reply_text(f"Я получил сообщение {upd.message.text}")
    print(upd.message.from_user)

if __name__ == '__main__':
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()