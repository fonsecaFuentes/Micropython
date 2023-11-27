from machine import ADC
import time

pin_sensor = 34

adc_sensor = ADC(pin_sensor)

while True:
    print(adc_sensor.read())
    time.sleep(1)
