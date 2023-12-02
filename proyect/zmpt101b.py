# Importar las librerías necesarias
import machine
import time


# Crear la clase ZMPT101B
class ZMPT101B:
    # Inicializar la clase con el pin y el voltaje de referencia
    def __init__(self, pin, vref):
        # Crear un objeto ADC para leer el pin analógico
        self.adc = machine.ADC(machine.Pin(pin))
        # Establecer el rango del ADC según el voltaje de referencia
        self.adc.atten(
            machine.ADC.ATTN_0DB if vref ==
            1.0 else machine.ADC.ATTN_2_5DB if vref ==
            1.4 else machine.ADC.ATTN_6DB if vref ==
            2.0 else machine.ADC.ATTN_11DB
        )
        # Establecer el valor medio del sensor como la mitad del rango del ADC
        self.offset = 2048 if vref == 1.0 else 4096
        # Establecer el factor de calibración como 1 por defecto
        self.calibration = 1
        # Establecer el voltaje RMS y la frecuencia como 0 por defecto
        self.voltage = 0
        self.frequency = 0

    # Calibrar el sensor con un valor conocido de voltaje RMS
    def calibrate(self, real_voltage):
        # Leer el valor máximo del sensor durante un ciclo
        max_value = 0
        start_time = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start_time) < 20:
            value = self.adc.read()
            if value > max_value:
                max_value = value
        # Calcular el factor de calibración como la relación
        # entre el voltaje real y el voltaje medido
        measured_voltage = (max_value - self.offset) * 0.707 * 0.0373
        self.calibration = real_voltage / measured_voltage

    # Obtener el voltaje RMS del sensor
    def getVoltage(self):
        # Leer el valor máximo y mínimo del sensor durante un ciclo
        max_value = 0
        min_value = 4096
        start_time = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start_time) < 20:
            value = self.adc.read()
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
        # Calcular el voltaje RMS usando el factor de calibración
        # y el valor medio del sensor
        self.voltage = ((max_value - min_value) / 2.0 -
                        self.offset) * 0.707 * 0.0373 * self.calibration
        # Devolver el voltaje RMS
        return self.voltage

    # Obtener la frecuencia del sensor
    def getFrequency(self):
        # Contar el número de cruces por cero del sensor durante un segundo
        zero_crosses = 0
        last_value = self.adc.read()
        start_time = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start_time) < 1000:
            value = self.adc.read()
            if (last_value < self.offset and value > self.offset) or (
                last_value > self.offset and value < self.offset
            ):
                zero_crosses += 1
            last_value = value
        # Calcular la frecuencia como la mitad del número de cruces por cero
        self.frequency = zero_crosses / 2.0
        # Devolver la frecuencia
        return self.frequency


# Crear un objeto de la clase ZMPT101B con el pin 34
# y el voltaje de referencia de 3.3V
sensor = ZMPT101B(33, 3.3)
# Calibrar el sensor con un valor conocido de 220V RMS
sensor.calibrate(220)
# Obtener el voltaje RMS y la frecuencia del sensor


def read_voltage():
    voltage = sensor.getVoltage()
    return voltage
# Imprimir los resultados
# print("Voltage: {:.2f} V".format(voltage))
# print("Frequency: {:.2f} Hz".format(frequency))
