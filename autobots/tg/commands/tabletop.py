from telegram import ReplyKeyboardMarkup
from commands.echo import echo
import random
from threading import Timer

def start(upd, ctx):
    start_kb = [['/dice', '/timer']]
    start_markup = ReplyKeyboardMarkup(start_kb)
    upd.message.reply_text("Выберите действие", reply_markup=start_markup)


timer_kb = [['30 секунд', '1 минута', '5 минут', 'Назад']]
def timer(upd, ctx):
    timer_markup = ReplyKeyboardMarkup(timer_kb)
    upd.message.reply_text("Выберите время", reply_markup=timer_markup)

def close(upd, ctx):
    t.cancel()
    upd.message.reply_text("Таймер сброшен")
    timer(upd, ctx)

t = None
time_text = ""
curr_upd = None

def timer_reply():
    curr_upd.message.reply_text(f"{time_text} истекло")
    timer(curr_upd, None)

def timer_handler(upd, ctx):
    if upd.message.text not in sum(timer_kb, []):
        echo(upd, ctx)
        return
    
    reply = ""
    time = 0
    
    match upd.message.text:
        case '30 секунд':
            time = 30
            reply = "30 секунд"
        case '1 минута':
            time = 60
            reply = "1 минуту"
        case '5 минут':
            time = 300
            reply = "5 минут"
        case 'Назад':
            start(upd, ctx)
            return

    global time_text, curr_upd, t
    time_text = reply
    curr_upd = upd
    
    upd.message.reply_text(f"Засёк {reply}", reply_markup=ReplyKeyboardMarkup([['/close']]))
    t = Timer(time, timer_reply)
    t.start()


dice_kb = [['Кинуть D6', 'Кинуть два D6'],
           ['Кинуть D20', 'Назад']]
def dice(upd, ctx):
    dice_markup = ReplyKeyboardMarkup(dice_kb)
    upd.message.reply_text("Выберите кубик", reply_markup=dice_markup)

def dice_handler(upd, ctx):
    #                          flatten dice_kb
    if upd.message.text not in sum(dice_kb, []):
        # default text handler
        timer_handler(upd, ctx)
        return
    
    reply = "s"
    match upd.message.text:
        case 'Кинуть D6':
            reply = f"{random.randint(1, 6)}"
        case 'Кинуть два D6':
            reply = f"{random.randint(1, 6)}, {random.randint(1, 6)}"
        case 'Кинуть D20':
            reply = f"{random.randint(1, 20)}"
        case 'Назад':
            start(upd, ctx)
            return
            
    upd.message.reply_text(reply)
    print(upd.message.from_user)