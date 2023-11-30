from machine import ADC
import math
import utime

VoltageAnalogInputPin = ADC(35)

voltajeOffset1 = 0
voltajeOffset2 = 0
voltajeSumarMuestras = 0
voltajeContadorMuestras = 0
voltajeUltimaLectura = utime.ticks_us()
lecturaMuesraOffset = 0
mediaVoltajeRMS = 0
sumaMuestraOffset = 0
offsetUltimaLectura = 0
contadorOffset = 0
# Variable para controlar el estado del offset
activarOffset = 1


def voltage_end():
    global voltajeOffset1
    global voltajeOffset2
    global voltajeSumarMuestras
    global voltajeContadorMuestras
    global lecturaMuesraOffset
    global voltajeUltimaLectura
    global mediaVoltajeOffset
    global mediaVoltajeRMS
    global sumaMuestraOffset

    # Chequea si se debe realizar el offset 1 o el offset 2
    if activarOffset == 1:
        setearOffset1()

    if activarOffset == 2:
        setearOffset2()

    # Realiza la lectura analógica cada 1 milisegundo
    if utime.ticks_us() >= voltajeUltimaLectura + 1000:
        if activarOffset > 0:
            # Lectura del offset durante el cálculo
            lecturaMuesraOffset = VoltageAnalogInputPin.read() - 512
            sumaMuestraOffset += lecturaMuesraOffset
            if activarOffset == 1:
                setearOffset1()
            if activarOffset == 2:
                setearOffset2()

    # Calcula el voltaje actual y acumula la suma de muestras al cuadrado
    voltajeActual = (VoltageAnalogInputPin.read() - 512) + voltajeOffset1
    voltajeSumarMuestras += voltajeActual ** 2
    voltajeContadorMuestras += 1
    voltajeUltimaLectura = utime.ticks_us()

    # Cuando se han acumulado 1000 lecturas
    if voltajeContadorMuestras == 1000:
        # Calcula la media del offset y el valor medio de las lecturas
        mediaVoltajeOffset = lecturaMuesraOffset / voltajeContadorMuestras
        voltajeMedio = voltajeSumarMuestras / voltajeContadorMuestras

        # Calcula el valor RMS
        mediaVoltajeRMS = (math.sqrt(voltajeMedio)) * 1.5

        # Ajusta el valor RMS con el offset2
        voltajeFinalRMS = mediaVoltajeRMS + voltajeOffset2

        # Evita valores negativos
        if voltajeFinalRMS <= 2.5:
            voltajeFinalRMS = 0

        # Resetea las variables para la siguiente iteración
        voltajeSumarMuestras = 0
        voltajeContadorMuestras = 0

        # Imprime el resultado por consola
        # print("El valor de voltaje RMS es: {} V".format(voltajeFinalRMS))
        return voltajeFinalRMS


def setearOffset1():
    global voltajeOffset1
    global offsetUltimaLectura
    global mediaVoltajeOffset
    global activarOffset
    global contadorOffset

    # Realiza una lectura cada 1 milisegundo
    if utime.ticks_us() >= offsetUltimaLectura + 1000:
        # Variable para contar el número de lecturas.
        contadorOffset += 1
        # Actualiza el tiempo para la siguiente lectura
        offsetUltimaLectura = utime.ticks_us()

    # Cuando se han realizado 1500 lecturas
    if contadorOffset == 1500:
        # Actualiza el offset1
        voltajeOffset1 = - mediaVoltajeOffset
        print(voltajeOffset1)
        # Pasamos a la siguiente etapa del cálculo del offset.
        activarOffset = 2
        # Reseteamos el contador.
        contadorOffset = 0


def setearOffset2():
    global voltajeOffset2
    global offsetUltimaLectura
    global mediaVoltajeRMS
    global activarOffset
    contadorOffset = 0

    # Realiza una lectura cada 1 milisegundo
    if utime.ticks_us() >= offsetUltimaLectura + 1000:
        # Variable para contar el número de lecturas.
        contadorOffset += 1
        # Actualiza el tiempo para la siguiente lectura
        offsetUltimaLectura = utime.ticks_us()

    # Cuando se han realizado 2500 lecturas
    if contadorOffset == 2500:
        # Actualiza el offset2
        voltajeOffset2 = - mediaVoltajeRMS
        # Termina el cálculo del offset
        activarOffset = 0
        # Resetea el contador
        contadorOffset = 0
        print("Fin de la calibración")


# while True:
#     voltage_end()
