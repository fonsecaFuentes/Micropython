from machine import ADC

# Configurar el pin al que está conectado el sensor ACS712
pin_sensor = 35
adc_sensor = ADC(pin_sensor)

# Configurar el divisor de voltaje con resistencias de 1800 ohms y 3300 ohms
r1 = 1800
r2 = 3300

# Calibrar la lectura del sensor
no_current_voltage = 2.5  # Voltaje cuando no hay consumo de corriente
sensitivity = 0.100  # Valor de sensibilidad según el Datasheet
adc_resolution = 4096  # Resolución del ADC (12 bits en este caso)
num_samples = 200


# Función para convertir la lectura del ADC a corriente en amperios
def convert_to_current(adc_value):
    # Calcular el voltaje de la lectura del ADC
    voltage = adc_value * (3.235 / adc_resolution)

    # Calcular la corriente en función de la calibración y el rango del sensor
    voltage_current = (voltage * (r1 + r2) / r2) + 0.05

    # La idea de la funcion max es, para asegurarnos de que el resultado
    # de la división anterior no sea negativo.
    # Si la expresión ... / sensor_sensitivity produce un valor negativo,
    # max lo ajustará a cero.
    current = max((voltage_current - no_current_voltage) / sensitivity, 0)

    return current


def average_current(adc_value):
    total_current = 0
    for i in range(num_samples):
        current_value = convert_to_current(adc_value)
        total_current += current_value
    average_current = total_current / num_samples
    return average_current


# Función para realizar la lectura del sensor
# y mostrar el resultado por consola
def read_current():
    adc_value = adc_sensor.read()
    current = average_current(adc_value)
    return current
