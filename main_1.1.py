from machine import Timer
import urequests
import ujson
from acs712 import read_current

# Configuración del sensor ACS712
sensor = read_current()

# Configuración del servidor
url = 'http://192.168.0.169'

# Contador de ejecuciones
executions_count = 0
# Número máximo de ejecuciones antes de detenerse
max_executions = 3


def post():
    global executions_count
    # Realizar una solicitud POST con las variables
    data = ujson.dumps({'Amperios': str(sensor)})
    response = urequests.post(url, json=data)
    # Verificar la respuesta
    if response.status_code == 200:
        print('Solicitud POST exitosa')
        print(response.text)
    else:
        print("Error: Request failed with status code", response.status_code)
        # Print the response content for debugging purposes
        print(response.text)
        executions_count += 1

        # Detener el temporizador después de un número máximo de ejecuciones
        if executions_count >= max_executions:
            # Detener el temporizador
            tim.deinit()

    # Cierra la conexión
    response.close()


tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC,  callback=lambda t: post())
