from machine import ADC, Pin
import time

sensibilidad = 0.1  # Ajuste de la sensibilidad para el sensor de 30 Amperios
ajuste = 0.05  # Sólo si es necesario,
# se usa para corregir posibles desvíos en la lectura


def setup():
    print("App start")


def loop():
    I = promedio_I(500)
    print("Intensidad:", I, "Amps")
    time.sleep_ms(100)

# Función para generar 500 muestras


def promedio_I(muestras_I):
    intencidad = 0
    for i in range(muestras_I):
        sensorA0 = adc_read_value() * (5.0 / 4095.0)
        intencidad += (sensorA0 - 2.5) / sensibilidad

    intencidad /= muestras_I
    return round(intencidad + ajuste, 2)

# Función para leer el valor analógico del pin A0


def adc_read_value():
    adc = ADC(Pin(34))  # Ajusta el pin según la conexión en tu ESP32
    return adc.read()


setup()

while True:
    loop()
