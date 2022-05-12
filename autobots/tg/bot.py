from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from commands.echo import echo

from commands.datetime import c_date as date, c_time as time
from commands.tabletop import start, dice, dice_handler, timer, close

from bot_tokens import BOT_TOKEN


if __name__ == '__main__':
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("timer", timer))
    dp.add_handler(CommandHandler("close", close))
    
    dp.add_handler(MessageHandler(Filters.text, dice_handler))
    
    updater.start_polling()
    updater.idle()