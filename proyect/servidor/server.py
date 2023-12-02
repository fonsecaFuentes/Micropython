from http.server import BaseHTTPRequestHandler, HTTPServer
from views2 import create_interface
from queue import Queue
import threading
from views2 import get_labels
import json

data_queue = Queue()


class S(BaseHTTPRequestHandler):
    amps = None
    voltage = None

    def _set_headers(self):
        self.send_response(200)
        self.send_header(keyword="Content-type", value="application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        json_data = {"prueba": "esto es una prueba"}
        json_to_pass = json.dumps(json_data)
        self.wfile.write(json_to_pass.encode("utf-8"))
        print("json enviado")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            # Decodificar el JSON recibido
            data = json.loads(post_data.decode('utf-8'))
            data = json.loads(data)

            S.amps = float(data.get('Amperios')) if data.get(
                'Amperios') is not None else None
            S.voltage = float(data.get('Voltaje')) if data.get(
                'Voltaje') is not None else None
            S.temp = float(data.get('Temperatura')) if data.get(
                'Temperatura') is not None else None
            S.hum = float(data.get('Humedad')) if data.get(
                'Humedad') is not None else None
            print("Datos recibidos:", data)
            data_queue.put((S.amps, S.voltage, S.temp, S.hum))

            self.send_response(200)
            self.end_headers()
            response_text = 'Solicitud POST recibida con éxito'
            self.wfile.write(response_text.encode('utf-8'))

        except json.JSONDecodeError as e:
            print('no logrado')
            self.send_response(400)
            self.end_headers()
            self.wfile.write(
                f'Error en el JSON recibido: {str(e)}'.encode('utf-8'))


def run_server(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ("", port)  # esto hace correr el servidor en el ip local
    servidor = server_class(server_address, handler_class)
    print("Starting server....")
    servidor.serve_forever()


def actualizar_valores():
    global temperatura_data  # Accede a la variable global
    global bar  # Accede a la variable global

    # Accede a las variables de instancia de la clase S
    temperatura = S.temperatura
    humedad = S.humedad
    amperios = S.amperios
    voltaje = S.voltaje

    # Obtener las etiquetas
    temp_label, hum_label, amps_label, voltage_label = get_labels()

    # Actualiza las etiquetas con los valores de S
    temp_label.config(text=f"Temperatura: {temperatura}")
    hum_label.config(text=f"Humedad: {humedad}")
    amps_label.config(text=f"Amperios: {amperios}")
    voltage_label.config(text=f"Voltaje: {voltaje}")

    # Actualiza los datos de temperatura para el gráfico
    temperatura_data[0] = temperatura

    if bar is not None:  # Verifica si bar no es None antes de acceder a él
        bar[0].set_height(temperatura_data[0])
        canvas.draw()

    # Programa una llamada a esta función nuevamente después de un tiempo
    ventana.after(1000, actualizar_valores)


if __name__ == "__main__":
    # Configura las variables de instancia de la clase S
    S.amps = None
    S.voltage = None
    S.temp = None
    S.hum = None


# Iniciar el servidor en un hilo separado
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

create_interface()
