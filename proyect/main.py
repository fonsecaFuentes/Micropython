from machine import Timer
import urequests
import ujson
from acs712 import read_current
from zmpt101b import voltage_end

# Configuración del sensor ACS712
sensor_acs712 = read_current()
sensor_zmpt101b = voltage_end()

# Configuración del servidor
url = 'http://192.168.0.137'

# Contador de ejecuciones
executions_count = 0
# Número máximo de ejecuciones antes de detenerse
max_executions = 3


def post():
    global executions_count
    response = None
    try:
        # Realizar una solicitud POST con las variables
        data = ujson.dumps(
            {'Amperios': str(sensor_acs712), 'Voltaje': str(sensor_zmpt101b)}
        )
        response = urequests.post(url, json=data)

        # Verificar la respuesta
        # Lanzará una excepción en caso de error HTTP
        response.raise_for_status()

        print('Solicitud POST exitosa')
        print(response.text)

    except Exception as e:
        print('Error:', str(e))
        print('---------------------------------')

        executions_count += 1

        # Detener el temporizador después de un número máximo de ejecuciones
        if executions_count >= max_executions:
            # Detener el temporizador
            tim.deinit()

    # Cierre de la conexión.
    if response:
        response.close()


tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC,  callback=lambda t: post())
