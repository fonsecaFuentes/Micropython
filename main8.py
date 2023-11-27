from machine import ADC
import time

# Configurar el pin al que está conectado el sensor ACS712
pin_sensor = 34
adc_sensor = ADC(pin_sensor)

# Configurar el divisor de voltaje con resistencias de 1800 ohms y 3300 ohms
r1 = 1800
r2 = 3300

# Calibrar la lectura del sensor
no_current_voltage = 2.5  # Voltaje cuando no hay consumo de corriente
sensitivity = 0.100  # Valor de sensibilidad según el Datasheet
adc_resolution = 4095  # Resolución del ADC (12 bits en este caso)

# Función para convertir la lectura del ADC a corriente en amperios


def convert_to_current(adc_value):
    # Calcular el voltaje de la lectura del ADC
    voltage = adc_value * (3.3 / adc_resolution)
    print("voltaje:", voltage)

    # Calcular la corriente en función de la calibración y el rango del sensor
    voltage_current = (voltage * (r1 + r2) / r2)
    print("voltage_current:", voltage_current)

    # La idea de la funcion max es, para asegurarnos de que el resultado
    # de la división anterior no sea negativo.
    # Si la expresión ... / sensor_sensitivity produce un valor negativo,
    # max lo ajustará a cero.
    current = max((voltage_current - no_current_voltage) / sensitivity, 0)

    return current

# Función para realizar la lectura del sensor
# y mostrar el resultado por consola


def read_current():
    adc_value = adc_sensor.read()
    print("Valor crudo del ADC:", adc_value)
    current = convert_to_current(adc_value)
    print("Corriente actual: {:.2f} A".format(current))
    return current


# Esta última parte del código lo copié de un usuario en git
# que encontré en una publicación
# Bucle principal para realizar lecturas continuas
try:
    while True:
        current_value = read_current()
        # Pausa de 1 segundo entre lecturas
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa detenido por el usuario.")
