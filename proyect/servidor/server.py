from http.server import BaseHTTPRequestHandler, HTTPServer
import values
import json


class S(BaseHTTPRequestHandler):
    amps = None
    voltage = None
    temp = None
    hum = None

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

            values.amps = float(data.get('Amperios')) if data.get(
                'Amperios') is not None else None
            values.voltage = float(data.get('Voltaje')) if data.get(
                'Voltaje') is not None else None
            values.temperatura = float(data.get('Temperatura')) if data.get(
                'Temperatura') is not None else None
            values.humedad = float(data.get('Humedad')) if data.get(
                'Humedad') is not None else None
            print("Datos recibidos:", data)

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

    # # Iniciar el servidor en un hilo separado
    # server_thread = threading.Thread(target=run_server)
    # server_thread.daemon = True
    # server_thread.start()
