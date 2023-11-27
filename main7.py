from machine import Pin, ADC
import time

# Pin definitions
adc_pin = Pin(34, mode=Pin.Down)
adc = ADC(adc_pin)
a1 = adc.read()
a = adc.atten(ADC.ATTN_11DB)
while True:
    print(a1)
    print(a)
    # print(v * (3.3 / 4095.0))
    time.sleep_ms(1000)
