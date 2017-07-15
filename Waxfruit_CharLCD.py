# coding=utf-8
"""
Waxfruit_CharLCD
5/18/2017 : 10:38 PM
Author : James L. Key
Modification of the Adafruit CharLCD module, it's neutered to work on windows for development purposes
"""

__author__ = 'James L. Key'
__project__ = 'CERMMorse'

# Original File
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

# Commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# Entry flags
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# Control flags
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# Move flags
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# Function set flags
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# Offset for up to 4 _rows.
LCD_ROW_OFFSETS = (0x00, 0x40, 0x14, 0x54)

# Char Lcd plate GPIO numbers.
LCD_PLATE_RS = 15
LCD_PLATE_RW = 14
LCD_PLATE_EN = 13
LCD_PLATE_D4 = 12
LCD_PLATE_D5 = 11
LCD_PLATE_D6 = 10
LCD_PLATE_D7 = 9
LCD_PLATE_RED = 6
LCD_PLATE_GREEN = 7
LCD_PLATE_BLUE = 8

# Char Lcd plate button names.
SELECT = 0
RIGHT = 1
DOWN = 2
UP = 3
LEFT = 4


class Adafruit_CharLCD(object):
    """Class to represent and interact with an HD44780 character Lcd display."""

    def __init__(self, rs, en, d4, d5, d6, d7, cols, lines, backlight=None,
                 invert_polarity=True,
                 enable_pwm=False,
                 gpio='',
                 pwm='',
                 initial_backlight=1.0):
        """Initialize the Lcd.  RS, EN, and D4...D7 parameters should be the pins
        connected to the Lcd RS, clock enable, and data line 4 through 7 connections.
        The Lcd will be used in its 4-bit mode so these 6 lines are the only ones
        required to use the Lcd.  You must also pass in the number of _columns and
        lines on the Lcd.  
        If you would like to control the backlight, pass in the pin connected to
        the backlight with the backlight parameter.  The invert_polarity boolean
        controls if the backlight is one with a LOW signal or HIGH signal.  The 
        default invert_polarity value is True, i.e. the backlight is on with a
        LOW signal.  
        You can enable PWM of the backlight pin to have finer control on the 
        brightness.  To enable PWM make sure your hardware supports PWM on the 
        provided backlight pin and set enable_pwm to True (the default is False).
        The appropriate PWM library will be used depending on the platform, but
        you can provide an explicit one with the pwm parameter.
        The initial state of the backlight is ON, but you can set it to an 
        explicit initial state with the initial_backlight parameter (0 is off,
        1 is on/full bright).
        You can optionally pass in an explicit GPIO class,
        for example if you want to use an MCP230xx GPIO extender.  If you don't
        pass in an GPIO instance, the default GPIO for the running platform will
        be used.
        """
        # Save column and line state.
        self._cols = cols
        self._lines = lines
        # Save GPIO state and pin numbers.
        self._gpio = gpio
        self._rs = rs
        self._en = en
        self._d4 = d4
        self._d5 = d5
        self._d6 = d6
        self._d7 = d7
        # Save backlight state.
        self._backlight = backlight
        self._pwm_enabled = enable_pwm
        self._pwm = pwm
        self._blpol = not invert_polarity

        self.displaycontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF
        self.displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_2LINE | LCD_5x8DOTS
        self.displaymode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT

    def home(self):
        """Move the cursor back to its home (first line and first column)."""
        print('Cursor to Home.\n')

    def clear(self):
        """Clear the Lcd."""
        print('Clear display.\n')

    def set_cursor(self, col, row):
        """Move the cursor to an explicit column and row position."""
        # Clamp row to the last row of the display.
        if row > self._lines:
            row = self._lines - 1
        # Set location.
        print('Move cursor to ' + str(col) + ' ' + str(row))

    def enable_display(self, enable):
        """Enable or disable the display.  Set enable to True to enable."""
        if enable:
            print('Enable Display')
        else:
            print('Disable Display')

    def show_cursor(self, show):
        """Show or hide the cursor.  Cursor is shown if show is True."""
        if show:
            print('Cursor Visible')
        else:
            print('Cursor Invisible')

    def blink(self, blink):
        """Turn on or off cursor blinking.  Set blink to True to enable blinking."""
        if blink:
            print('Blink Cursor')
        else:
            print('Stop Cursor Blink')

    def move_left(self):
        """Move display left one position."""
        print('Cursor Left')

    def move_right(self):
        """Move display right one position."""
        print('Cursor Right')

    def set_left_to_right(self):
        """Set text direction left to right."""
        print('Text Direction Left to Right')

    def set_right_to_left(self):
        """Set text direction right to left."""
        print('Text Direction Right to Left')

    def autoscroll(self, autoscroll):
        """Autoscroll will 'right justify' text from the cursor if set True,
        otherwise it will 'left justify' the text.
        """
        if autoscroll:
            print('Autoscroll Enabled')
        else:
            print('Autoscroll Disabled')

    def message(self, text):
        """Write text to display.  Note that text can include newlines."""
        line = 0
        # Iterate through each character.
        for char in text:
            # Advance to next line if character is a new line.
            if char == '\n':
                print('\n')
                # Move to left or right side depending on text direction.
                col = 0 if self.displaymode & LCD_ENTRYLEFT > 0 else self._cols - 1
                self.set_cursor(col, line)
            # Write the character to the display.
            else:
                self.write8(ord(char), True)

    def set_backlight(self, backlight):
        """Enable or disable the backlight.  If PWM is not enabled (default), a
        non-zero backlight value will turn on the backlight and a zero value will
        turn it off.  If PWM is enabled, backlight can be any value from 0.0 to
        1.0, with 1.0 being full intensity backlight.
        """
        if self._backlight is not None:
            print('Backlight ON')
        else:
            print('Backlight OFF')

    def write8(self, value, char_mode=False):
        """Write 8-bit value in character or data mode.  Value should be an int
        value from 0-255, and char_mode is True if character data or False if
        non-character data (default).
        """
        # One millisecond delay to prevent writing too quickly.
        self._delay_microseconds(1000)
        # Set character / data bit.

        if char_mode is True:
            print(str(value))
        else:
            print(hex(value))

    def create_char(self, location, pattern):
        """Fill one of the first 8 CGRAM locations with custom characters.
        The location parameter should be between 0 and 7 and pattern should
        provide an array of 8 bytes containing the pattern. E.g. you can easyly
        design your custom character at http://www.quinapalus.com/hd44780udg.html
        To show your custom character use eg. lcd._message('\x01')
        """
        # only position 0..7 are allowed
        location &= 0x7
        self.write8(LCD_SETCGRAMADDR | (location << 3))
        for i in range(8):
            self.write8(pattern[i], char_mode=True)

    def _delay_microseconds(self, microseconds):
        # Busy wait in loop because delays are generally very short (few microseconds).
        end = time.time() + (microseconds / 1000000.0)
        while time.time() < end:
            pass

    def _pulse_enable(self):
        # Pulse the clock enable line off, on, off to send command.
        pass

    def _pwm_duty_cycle(self, intensity):
        # Convert intensity value of 0.0 to 1.0 to a duty cycle of 0.0 to 100.0
        pass


class Adafruit_RGBCharLCD(Adafruit_CharLCD):
    """Class to represent and interact with an HD44780 character Lcd display with
    an RGB backlight."""

    def __init__(self, rs, en, d4, d5, d6, d7, cols, lines, red, green, blue,
                 gpio='',
                 invert_polarity=True,
                 enable_pwm=False,
                 pwm='',
                 initial_color=(1.0, 1.0, 1.0)):
        """Initialize the Lcd with RGB backlight.  RS, EN, and D4...D7 parameters 
        should be the pins connected to the Lcd RS, clock enable, and data line 
        4 through 7 connections. The Lcd will be used in its 4-bit mode so these 
        6 lines are the only ones required to use the Lcd.  You must also pass in
        the number of _columns and lines on the Lcd.
        The red, green, and blue parameters define the pins which are connected
        to the appropriate backlight LEDs.  The invert_polarity parameter is a
        boolean that controls if the LEDs are on with a LOW or HIGH signal.  By
        default invert_polarity is True, i.e. the backlight LEDs are on with a
        low signal.  If you want to enable PWM on the backlight LEDs (for finer
        control of colors) and the hardware supports PWM on the provided pins,
        set enable_pwm to True.  Finally you can set an explicit initial backlight
        color with the initial_color parameter.  The default initial color is
        white (all LEDs lit).
        You can optionally pass in an explicit GPIO class,
        for example if you want to use an MCP230xx GPIO extender.  If you don't
        pass in an GPIO instance, the default GPIO for the running platform will
        be used.
        """
        super(Adafruit_RGBCharLCD, self).__init__(rs, en, d4, d5, d6, d7,
                                                  cols,
                                                  lines,
                                                  enable_pwm=enable_pwm,
                                                  backlight=None,
                                                  invert_polarity=invert_polarity,
                                                  gpio=gpio,
                                                  pwm=pwm)
        self._red = red
        self._green = green
        self._blue = blue
        # Setup backlight pins.

    def _rgb_to_duty_cycle(self, rgb):
        # Convert tuple of RGB 0-1 values to tuple of duty cycles (0-100).
        pass

    def _rgb_to_pins(self, rgb):
        # Convert tuple of RGB 0-1 values to dict of pin values.
        pass

    def set_color(self, red, green, blue):
        """Set backlight color to provided red, green, and blue values.  If PWM
        is enabled then color components can be values from 0.0 to 1.0, otherwise
        components should be zero for off and non-zero for on.
        """
        print(red, green, blue)

    def set_backlight(self, backlight):
        """Enable or disable the backlight.  If PWM is not enabled (default), a
        non-zero backlight value will turn on the backlight and a zero value will
        turn it off.  If PWM is enabled, backlight can be any value from 0.0 to
        1.0, with 1.0 being full intensity backlight.  On an RGB display this
        function will set the backlight to all white.
        """
        self.set_color(backlight, backlight, backlight)


class Adafruit_CharLCDPlate(Adafruit_RGBCharLCD):
    """Class to represent and interact with an Adafruit Raspberry Pi character
    Lcd plate."""

    def __init__(self, address=0x20, busnum='', cols=16, lines=2):
        """Initialize the character Lcd plate.  Can optionally specify a separate
        I2C address or bus number, but the defaults should suffice for most needs.
        Can also optionally specify the number of _columns and lines on the Lcd
        (default is 16x2).
        """
        # Configure MCP23017 device.

        # Set Lcd R/W pin to low for writing only.

        # Set buttons as inputs with pull-ups enabled.

        # Initialize Lcd (with no PWM support).
        super(Adafruit_CharLCDPlate, self).__init__(LCD_PLATE_RS, LCD_PLATE_EN,
                                                    LCD_PLATE_D4, LCD_PLATE_D5, LCD_PLATE_D6, LCD_PLATE_D7, cols, lines,
                                                    LCD_PLATE_RED, LCD_PLATE_GREEN, LCD_PLATE_BLUE, enable_pwm=False,
                                                    gpio='')

    def is_pressed(self, button):
        """Return True if the provided button is pressed, False otherwise."""
        print('Checking Button')
        return 1
