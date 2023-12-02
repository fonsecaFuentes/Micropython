from machine import Pin
import dht

sensor = dht.DHT22(Pin(32))


def read_dht22():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    data = {'Temperatura': temp, 'Humedad': hum}
    return data
