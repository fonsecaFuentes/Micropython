from tkinter import Button
from tkinter import Label
from tkinter import StringVar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from server import data_queue


class LineGraph:
    def __init__(self, master, row, rowspan, column, columnspan, figsize):
        # Crear una figura y un eje
        self.fig, self.ax = plt.subplots(figsize=figsize)

        # Crear un canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().grid(
            row=row, rowspan=rowspan, column=column, columnspan=columnspan
        )

    def update_graph(self, x, y):
        # Dibujar el gráfico de líneas
        self.ax.plot(x, y)

        # Mostrar el gráfico en el canvas
        self.canvas.draw()


# Clase MyButton para crear botones personalizados
class MyButton():
    def __init__(
        self, parent,
        text, command,
        row, column,
        sticky, pady,
        padx
    ):
        self.button = Button(parent, text=text, command=command)
        self.button.grid(
            row=row,
            column=column,
            sticky=sticky,
            padx=padx,
            pady=pady
        )


# Clase MyLabel para crear etiquetas personalizadas
class MyLabel():
    def __init__(
        self, parent,
        text,
        row,
        column,
        sticky,
        pady,
        padx
    ):
        self.label = Label(parent, text=text)
        self.label.grid(
            row=row,
            column=column,
            sticky=sticky,
            padx=padx,
            pady=pady
        )

    def configure(self, **kwargs):
        self.label.configure(**kwargs)


# Clase MyLayout para crear diseños personalizados
class MyLayout(MyLabel):
    def __init__(
        self, text,
        bg, fg,
        width,
        row,
        rowspan,
        column,
        columnspan,
        sticky,
        pady,
        padx
    ):
        self.layout = Label(
            text=text, bg=bg, fg=fg, width=width
        )
        self.layout.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
            pady=pady,
            padx=padx
        )


class Interface():
    def __init__(self, master):
        self.master = master
        self.closing = False
        self.color = "#FB0909"

        self.master.title('Interfaz')

        # Variables para amperios y voltaje
        self.amps_value = StringVar()
        self.voltage_value = StringVar()

        # labels y layout
        self.layout_amps = MyLayout(
            text="Amperios",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=0,
            rowspan=2,
            column=0,
            columnspan=5,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.layout_voltage = MyLayout(
            text="Voltaje",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=3,
            rowspan=2,
            column=0,
            columnspan=5,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.layout_amps_graph = MyLayout(
            text="Amperios Gráfica",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=7,
            rowspan=2,
            column=0,
            columnspan=5,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.layout_graph_voltage = MyLayout(
            text="Voltaje Gráfica",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=12,
            rowspan=2,
            column=0,
            columnspan=5,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.layout_relay = MyLayout(
            text="Relay",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=18,
            rowspan=2,
            column=0,
            columnspan=5,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.relay_indicator1 = MyLayout(
            text="",
            bg=self.color,
            fg="#000000",
            width=10,
            row=21,
            rowspan=1,
            column=0,
            columnspan=1,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.relay_indicator2 = MyLayout(
            text="",
            bg=self.color,
            fg="#000000",
            width=10,
            row=21,
            rowspan=1,
            column=1,
            columnspan=1,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.relay_indicator3 = MyLayout(
            text="",
            bg=self.color,
            fg="#000000",
            width=10,
            row=21,
            rowspan=1,
            column=2,
            columnspan=1,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.relay_indicator4 = MyLayout(
            text="",
            bg=self.color,
            fg="#000000",
            width=10,
            row=21,
            rowspan=1,
            column=3,
            columnspan=1,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.amps = MyLabel(
                self.master,
                text="Amperios:",
                row=2, column=1, sticky="w", pady=2, padx=2
            )

        self.voltage = MyLabel(
                self.master,
                text="Voltaje:",
                row=5, column=1, sticky="w", pady=2, padx=2
            )

        # Botones
        self.boton_relay1 = MyButton(
            self.master,
            text="ENCENDER",
            command=lambda: self.data_management.modify_item(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.forms
            ),
            row=20, column=0, sticky="nsew", pady=8, padx=8
        )

        self.boton_relay2 = MyButton(
            self.master,
            text="ENCENDER",
            command=lambda: self.data_management.modify_item(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.forms
            ),
            row=20, column=1, sticky="nsew", pady=8, padx=8
        )

        self.boton_relay3 = MyButton(
            self.master,
            text="ENCENDER",
            command=lambda: self.data_management.modify_item(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.forms
            ),
            row=20, column=2, sticky="nsew", pady=8, padx=8
        )

        self.boton_relay4 = MyButton(
            self.master,
            text="ENCENDER",
            command=lambda: self.data_management.modify_item(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.forms
            ),
            row=20, column=3, sticky="nsew", pady=8, padx=8
        )

        # Graficas
        self.current_graph = LineGraph(
            self.master,
            row=9,
            rowspan=2,
            column=0,
            columnspan=4,
            figsize=(4, 2.5)
            )
        self.voltage_graph = LineGraph(
            self.master,
            row=15,
            rowspan=2,
            column=0,
            columnspan=4,
            figsize=(4, 2.5)
            )
        # self.temperature_graph = LineGraph(self.master, row=9, column=0)
        # self.humidity_graph = LineGraph(self.master, row=10, column=0)


interface = Interface()


# La función update se encarga de actualizar los datos en la interfaz gráfica
def update(interface, data_queue):
    # Comprobar si la ventana todavía existe
    if interface.master.winfo_exists():
        # Leer los datos de la cola
        while not data_queue.empty():
            amps, voltage = data_queue.get()
            print(amps, voltage)

            # Actualizar las graficas con los nuevos datos
            interface.current_graph.update_graph(amps)
            interface.voltage_graph.update_graph(voltage)

            # Actualizar las etiquetas con los nuevos datos
            interface.amps.config(text=f"Amperios: {amps}")
            interface.voltage.config(text=f"Voltaje: {voltage}")

            # Solo programar la próxima actualización si la
            # ventana no se está cerrando
            if not interface.closing:
                interface.master.after(1000, update, interface, data_queue)

        # # Actualización de etiquetas y gráficos en la interfaz gráfica
        # self.master.after(1000, self.update)
