from time import sleep
import functions as bot
import colors
loops_done = 0
print("Starting bot...\nSleeping for 5 seconds before begining.")
sleep(5)

while True:
    if bot.is_magic_open():
        bot.cast_alch()
        sleep(bot.get_delay())
        bot.cast_tele()
        sleep(1.5)
        loops =+ 1