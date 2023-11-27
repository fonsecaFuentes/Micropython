import network
import utime


# import gc
# gc.collect()

# ssid = "wilu"
# password = '9,-E"$_z/L."'

ap = network.WLAN(network.STA_IF)
ap.active(True)
redes = ap.scan()

for red in redes:
    print(red[0].decode() + ' ' + str(red[3]))

ap.connect('wilu', '9,-E"$_z/L."')

while not ap.isconnected():
    print('.')
    utime.sleep(1)

print(ap.ifconfig()[0])
