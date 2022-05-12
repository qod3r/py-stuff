import time

def c_date(upd, ctx):
    upd.message.reply_text(time.strftime("%d.%m.%Y"))
    
def c_time(upd, ctx):
    upd.message.reply_text(time.strftime("%H:%M:%S"))
