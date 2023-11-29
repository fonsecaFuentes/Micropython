from modelo2 import Interface
from tkinter import Tk


class Controller:
    def __init__(self, root):
        # Asignar ventana raiz
        self.root = root
        # Crear la ventana principal
        self.view = Interface(self.root)


if __name__ == '__main__':
    # Crear la ventana principal
    master = Tk()
    app = Controller(master)
    master.mainloop()
