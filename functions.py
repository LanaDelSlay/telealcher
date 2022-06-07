import os
import numpy
import colors
import pyclick
import pyautogui
from time import sleep


pyautogui.FAILSAFE = False

def is_magic_open():
    if pyautogui.locateCenterOnScreen('./imgs/magicOpen.png'):
        return True
    else:
        return False
       
def click(x,y):
    hc = pyclick.HumanClicker()
    hc.move((x,y), get_delay())
    hc.click()
    
def click_color(color):
    s = pyautogui.screenshot()
    for x in range(0,1919,5):
        for y in range(0,1079,5):
            if s.getpixel((x, y)) == color:
                newCoords = get_coords_delay_alch(x, y)
                click(newCoords[0],newCoords[1])
                return()
    
def click_tele(color):
    colorsS = colors.camelot_tele
    s = pyautogui.screenshot()
    for x in range(1919,0,-1):
        for y in range(1079, 0,-1):
            if s.getpixel((x, y)) == colors.camelot_tele:
                newCoords = get_coords_delay_tele(x, y)
                click(newCoords[0],newCoords[1])
                return()
    
    
def cast_alch():
    click_color(colors.alch_item_screen_marker_color)
    sleep(get_delay())  
    pyclick.HumanClicker().click()      

def cast_tele():
    click_tele(colors.camelot_tele)
    sleep(get_delay())  
    pyclick.HumanClicker().click()      

def get_delay():
    deviation = numpy.random.normal(loc=.7, scale=1.2, size=(2))
    delay = abs((round(deviation[1], 2))) # Absolute value for no negatives, and rounding to two decimals.
    if (delay < .2):
        delay += .4
    if (delay > 2):
        delay -= .75
    return delay

def get_coords_delay_alch(x,y):
    deviation = numpy.random.normal(loc=9, scale=5, size=(2))
    deviation = deviation.astype(int)
    delay_x = abs((round(deviation[0], 0))) # Absolute value for no negatives, and rounding to two decimals.
    delay_y = abs((round(deviation[1], 0))) 
    coords = [(delay_x + x), (delay_y + y)]
    return coords

def get_coords_delay_tele(x,y):
    deviation = numpy.random.normal(loc=11, scale=15, size=(2))
    deviation = deviation.astype(int)
    delay_x = -abs((round(deviation[0], 0))) # Absolute value for no negatives, and rounding to two decimals.
    delay_y = -abs((round(deviation[1], 0))) 
    coords = [(delay_x + x), (delay_y + y)]
    return coords
