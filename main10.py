from machine import ADC
from machine import Timer
import math
import time


# Configurar el pin al que está conectado el sensor ZMPT101B
pin_sensor = 35
adc_sensor = ADC(pin_sensor)
voltage_final_rms = 0.0
voltage_mean = 0.0
voltage_actual = 0.0
voltage_last_sample = 0
voltage_sample_sum = 0.0
voltage_sample_count = 0
voltage_offset1 = 0.0
voltage_offset2 = 0.0


def set_offset1(timer):
    global voltage_offset1
    global voltage_sample_count
    global voltage_sample_sum
    voltage_offset1 = -voltage_sample_sum / voltage_sample_count
    timer.deinit()


def set_offset2(timer):
    global voltage_offset2
    global voltage_mean
    voltage_offset2 = -voltage_mean
    timer.deinit()


def setup():
    global voltage_offset1
    global voltage_offset2
    global voltage_sample_sum
    global voltage_sample_count
    global voltage_mean

    print("Inicio de Calibracion")

    voltage_offset1_timer = Timer(-1)
    voltage_offset1_timer.init(
        period=1000, mode=Timer.ONE_SHOT, callback=set_offset1)

    while voltage_offset1_timer.deinit() is None:
        voltage_sample_read = adc_sensor.read() - 2048
        voltage_sample_sum += voltage_sample_read
        voltage_sample_count += 1

    voltage_offset2_timer = Timer(-1)
    voltage_offset2_timer.init(
        period=1000, mode=Timer.ONE_SHOT, callback=set_offset2)

    while voltage_offset2_timer.deinit() is None:
        voltage_sample_read = adc_sensor.read() - 2048
        voltage_mean += voltage_sample_read

    print("Fin Calibracion")


def loop():
    global voltage_actual
    global voltage_last_sample
    global voltage_sample_sum
    global voltage_sample_count
    global voltage_mean
    global voltage_final_rms
    global voltage_offset2

    if time.ticks_us() >= voltage_last_sample + 1000:
        voltage_sample_read = (
            adc_sensor.read() - 2048
        ) + voltage_offset1
        voltage_sample_sum += voltage_sample_read ** 2
        voltage_sample_count += 1
        voltage_last_sample = time.ticks_us()

    if voltage_sample_count == 1000:
        voltage_mean = voltage_sample_sum / voltage_sample_count
        rms_voltage_mean = math.sqrt(voltage_mean) * 1.5
        # adjust_rms_voltage_mean = rms_voltage_mean + voltage_offset2
        voltage_final_rms = rms_voltage_mean + voltage_offset2
        if voltage_final_rms <= 2.5:
            voltage_final_rms = 0

        print("El valor de voltaje RMS es: {:.2f} V".format(voltage_final_rms))

        voltage_sample_sum = 0.0
        voltage_sample_count = 0


# Llamamos a la función setup una vez al inicio
setup()

# El bucle principal se ejecutará continuamente
while True:
    loop()
