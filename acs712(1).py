from machine import Pin, ADC
import sys
import time
import math


class ACS712:
    def __init__(self, ACS712type=20, pin=34):
        self._zero = 512
        self._sensitivity = 0
        self._pin = pin
        self.ADC_SCALE = 1023.0
        self.VREF = 5.0
        self.DEFAULT_FREQUENCY = 50
        self._adc = None

        if (ACS712type == 5):
            self._sensitivity = 0.185
        elif (ACS712type == 20):
            self._sensitivity = 0.100
        else:
            self._sensitivity = 0.066

    def calibrate(self):
        acc = 0
        if (sys.platform == 'esp8266'):
            self._adc = ADC(self._pin)
        elif (sys.platform == 'esp32'):
            self._adc = ADC(Pin(self._pin))
            self.ADC_SCALE = 4095

        for i in range(0, 10):
            acc += self._adc.read()

        self._zero = acc / 10

        return self._zero

    @property
    def zeroPoint(self):
        return self._zero

    @zeroPoint.setter
    def zeroPoint(self, _zero):
        self._zero = _zero

    @property
    def sensitivity(self):
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, value):
        self._sensitivity = value

    def getCurrentDC(self):
        acc = 0

        for i in range(0, 10):
            acc += self._adc.read() - self._zero

        I = acc / 10.0 / self.ADC_SCALE * self.VREF / self._sensitivity

        return I

    def getCurrentAC(self, freq=50):
        period = 10000 / freq
        t_start = int(time.ticks_ms() / 100)
        Isum = 0
        msr_cnt = 0
        Inow = None

        while ((time.ticks_ms() / 100) - t_start < period):
            Inow = self._adc.read() - self.zeroPoint
            Isum += Inow * Inow
            msr_cnt += 1
        pass

        Irms = math.sqrt(Isum / msr_cnt) / self.ADC_SCALE * \
            self.VREF / self._sensitivity
        return Irms
