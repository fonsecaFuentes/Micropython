from machine import ADC, Pin
import time

adc_pin = Pin(34, mode=Pin.IN)
adc = ADC(adc_pin)

rep = 0

while True:
    v = adc.read()
    # print(v)
    print(v * (3.3 / 4095.0))
    time.sleep_ms(1000)
