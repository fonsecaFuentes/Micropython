from machine import Pin, ADC
import utime

sensibilidad = 0.100
v = 0
ruido = 0.040
selector_pin = ADC(Pin(34))

reposo = 2.5
pico = 0
redelectrica = 220


def setup():
    print("Inicio")


def voltaje():
    global v
    v = adc_read_value() * (3.3 / 1023.0)


def directa():
    global v
    salida = 0
    intensidad = 0

    for i in range(500):
        voltaje()
        intensidad += (v - 2.5) / sensibilidad

    intensidad /= 500
    salida = intensidad

    if salida <= ruido:
        salida = 0

    print("Directa:", salida)
    utime.sleep_ms(250)


def alterna():
    global v, pico, redelectrica
    tiempo = utime.ticks_ms()
    maxima = 0
    minima = 0

    while utime.ticks_ms() - tiempo < 500:
        voltaje()
        intensidad = 0.9 * intensidad + 0.1 * ((v - reposo) / sensibilidad)

        if intensidad > maxima:
            maxima = intensidad

        if intensidad < minima:
            minima = intensidad

    salida = ((maxima - minima) / 2)

    if salida <= ruido:
        salida = 0

    print("Alterna:", salida)
    utime.sleep_ms(300)


def adc_read_value():
    adc = ADC(Pin(34))  # Ajusta el pin según la conexión en tu ESP32
    return adc.read()


setup()

while True:
    directa()
    voltaje()
    alterna()
