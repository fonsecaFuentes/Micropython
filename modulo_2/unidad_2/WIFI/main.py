import network

ssid = "wilu"
password = '9,-E"$_z/L."'

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print("conectando a la red")
    sta_if.active(True)
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        print("conectando")
print("configuracion de red:", sta_if.ifconfig())
