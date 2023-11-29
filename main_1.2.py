from machine import ADC, Pin
import time

# Configurar el pin
adc_sensor = ADC(34)

# Voltaje cuando no hay consumo de corriente
sensor_no_voltage = 2.5
# Sensibilidad en Voltios/Amperio para sensor de 20A
sensor_sensitivity = 0.100
# Resolución del ADC (12 bits en este caso)
adc_resolution = 4095


# Función para convertir la lectura del ADC a corriente en amperios
def convert_to_current(adc_value):
    # Calcular el voltaje de la lectura del ADC
    voltage = adc_value * (3.3 / adc_resolution)

    # Ecuación  para obtener la corriente
    current = (voltage - sensor_no_voltage) / sensor_sensitivity

    return current


# Función para realizar la lectura del sensor
# y mostrar el resultado por consola
def read_current():
    adc_value = adc_sensor.read()
    current = convert_to_current(adc_value)
    print("Corriente actual: {:.2f} A".format(current))
    return current


#  Bucle principal para realizar lecturas continuas
while True:
    current_value = read_current()
    time.sleep(1)
