'''
5/18/2017 : 10:38 PM
Author : James L. Key
Modification of the Adafruit CharLCD module, it's neutered to work on windows for development purposes
'''

import os
if os.name == 'nt':
    import Waxfruit_CharLCD as Lcd
else:
    import Adafruit_CharLCD as Lcd

lcd = Lcd.Adafruit_CharLCDPlate()  # or similar depending on Hardware

lcd.clear()
lcd.set_color(1, 0, 0)  # once again depending on Hardware
lcd.message('Hello World')
lcd.set_cursor(0, 1)
