import lcd
import apiClient
from time import sleep
import relay
import temperature

while(True):
    data = apiClient.getData()
    temp = temperature.read_temp()
    temp_update_response = apiClient.updateTemp(temp)
    temp_setting = data['temp_set']
    light = data['light_1']
    light = int(light)
    lcd.update_lcd(f"Temperatura: {temp}C\nTemp. set.: {temp_setting}C")
    sleep(3)

    if light == 1:
        relay.high()
    else:
        relay.low()
