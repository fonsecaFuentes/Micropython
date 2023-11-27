# from website import mi_web
from machine import Pin
import network
import socket


ssid = "wilu"
password = '9,-E"$_z/L."'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print("Conexion: {}".format(ssid))
print(wlan.ifconfig())

out = Pin(22, Pin.OUT)


def mi_web():
    html = """
    <!Doctype html>
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <head>
        <body>
            <div class="container">
                <div class="row">
                    <h1>Hola Wilson</h1>
                    <img src="https://sine-quo-non.com/media/aire_libre/2023/03/12/airelibre_prCubMc.png" />
                </div>
            </div>
        </body>
    <html>
    """
    return html


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))
tcp_socket.listen(3)

while True:
    conn, addr = tcp_socket.accept()
    print('Nueva conexion desde {}'.format(str(addr)))
    request = conn.recv(1024)
    print('Solicitud {}'.format(str(request)))
    request = str(request)

    if request.find('usuario=wilson'):
        print('Wilson')

    response = mi_web()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-Type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()
