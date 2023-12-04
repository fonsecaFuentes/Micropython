from views import Interface
from server import run_server
from tkinter import Tk
import threading
from sys import argv


class Controller:
    def __init__(self, root):
        # Asignar ventana raiz
        self.root = root
        # Crear la ventana principal
        self.view = Interface(self.root)
        # # Llamar a la función update para actualizar
        # # los datos en la interfaz gráfica
        # self.view.update()

    def on_close(self):
        # Establecer una bandera para indicar que la ventana se está cerrando
        self.view.closing = True
        self.root.destroy()


if __name__ == '__main__':
    # Creamos y comenzamos un nuevo hilo para el servidor
    if len(argv) == 2:
        server_therad = threading.Thread(
            target=run_server, args=(int(argv[1]),)
        )
    else:
        server_therad = threading.Thread(target=run_server)
    server_therad.start()

    # Crear la ventana principal
    master = Tk()
    app = Controller(master)
    # Evento de cierre de ventana, establece la función
    # on_close como la función de cierre de la ventana
    master.protocol("WM_DELETE_WINDOW", app.on_close)
    master.mainloop()
