from machine import ADC, Pin
import time

sensor_pin = 34
mV_per_Amp = 185
Watt = 0
Voltage = 0
VRMS = 0
AmpsRMS = 0


def setup():
    print("ACS712 current sensor")


def getVPP():
    result = 0.0
    read_values = []
    start_time = time.ticks_ms()

    while (time.ticks_ms() - start_time) < 1000:
        read_value = adc.read()
        read_values.append(read_value)

    max_value = max(read_values)
    min_value = min(read_values)

    result = ((max_value - min_value) * 3.3) / 4096.0

    return result


def loop():
    while True:
        print("")
        Voltage = getVPP()
        VRMS = (Voltage / 2.0) * 0.707
        AmpsRMS = ((VRMS * 1000) / mV_per_Amp) - 0.3
        print("{:.2f} Amps RMS  ---  ".format(AmpsRMS))
        Watt = int(AmpsRMS * 240 / 1.2)
        print("{} Watts".format(Watt))
        time.sleep_ms(1000)


# Configuración inicial
adc = ADC(Pin(sensor_pin))
setup()

# Bucle principal
loop()
