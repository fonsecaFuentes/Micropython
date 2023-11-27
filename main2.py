from acs712 import ACS712


class clsMain:
    def __init__(self):
        pass

    def main(self):
        acs = ACS712()
        acs.calibrate()
        print("Zeropoint=", acs.zeroPoint, "sensitivity=", acs.sensitivity)

        for i in range(1, 50):
            currA = acs.getCurrentAC(freq=50)
            print("Amps=", currA)


print("App start")
m1 = clsMain()
m1.main()
print("App eind")
