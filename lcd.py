import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono

lcd_columns = 16
lcd_rows = 2
lcd_rs = DigitalInOut(board.D26)
lcd_en = DigitalInOut(board.D19)
lcd_d4 = DigitalInOut(board.D13)
lcd_d5 = DigitalInOut(board.D6)
lcd_d6 = DigitalInOut(board.D5)
lcd_d7 = DigitalInOut(board.D11)

lcd = Character_LCD_Mono(
	lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

def update_lcd(message):
	lcd.message = message

