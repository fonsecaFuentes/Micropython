from acs712 import ACS712
from machine import Pin, ADC

# Configura el pin al que está conectado el sensor ACS712
pin_sensor = 32  # Ajusta el número de pin según tu configuración
analog_pin = ADC(Pin(pin_sensor))
analog_value = analog_pin.read()
print("Valor analógico: {}".format(analog_value))

# Crea una instancia de ACS712 con sensibilidad de 100mV/A
acs = ACS712(20, pin_sensor)  # 5 para ACS712-05, ajusta según tu modelo

# Calibra el sensor
acs.calibrate()

# Lee la corriente en amperios (valor DC)
current_dc = acs.getCurrentDC()
print("Corriente DC: {} A".format(current_dc))

# Lee la corriente en amperios (valor AC)
# Frecuencia de la corriente alterna (ajusta según sea necesario)
current_ac = acs.getCurrentAC(freq=50)
print("Corriente AC: {} A".format(current_ac))
