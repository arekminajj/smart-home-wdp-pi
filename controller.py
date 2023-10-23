import lcd
import apiClient
from time import sleep

while(True):
    data = apiClient.getData()
    temp = data['temp']
    temp_setting = data['temp-set']
    light = data['light_1']
    lcd.update_lcd(f"Temperature: {temp}C\nTemp. set.: {temp_setting}C")
    sleep(10)
