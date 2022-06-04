from time import sleep
import functions as bot

while True:
    if bot.is_magic_open():
        bot.cast_alch()
        sleep(bot.get_delay())
        bot.cast_tele()
        sleep(2)