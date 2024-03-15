from machine import Pin,I2C,ADC
light-pin = pin(26)
adc = ADC(light-pin)
light-intensity = adc.read_u16()

light ="light :" + str(light-intensity)
oled.text:(light)
oled.show()

