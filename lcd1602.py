from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)

def LCD_init():
    lcd = LCD()
    return lcd

def LCD_clear():
    lcd.clear()

def LCD_show(line1="", line2=""):
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text(line1, 1)
    lcd.text(line2, 2)

if __name__ == '__main__':
    LCD_show("first", "second")
    time.sleep(3)
    LCD_show("test")