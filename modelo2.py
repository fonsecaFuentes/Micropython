from tkinter import Button
from tkinter import Label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LineGraph:
    def __init__(self, master, row, column):
        # Crear una figura y un eje
        self.fig, self.ax = plt.subplots()

        # Crear un canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().grid(row=row, column=column)

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

    def configure(self, **kwargs):
        self.button.configure(**kwargs)


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

        self.master.title('Interfaz')

        self.current_data = [0]
        self.voltage_data = [0]
        self.line = None
        self.canvas = None

        # labels
        self.final_work = MyLayout(
            text="TRABAJO FINAL",
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

        self.search = MyLabel(
                self.master,
                text="BUSCAR:",
                row=2, column=2, sticky="w", pady=2, padx=2
            )

        self.search = MyLabel(
                self.master,
                text="BUSCAR:",
                row=2, column=3, sticky="w", pady=2, padx=2
            )

        self.final_work = MyLayout(
            text="TRABAJO FINAL",
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

        self.search = MyLabel(
                self.master,
                text="BUSCAR:",
                row=5, column=2, sticky="w", pady=2, padx=2
            )

        self.search = MyLabel(
                self.master,
                text="BUSCAR:",
                row=5, column=3, sticky="w", pady=2, padx=2
            )

        # # Datos para el eje X y el eje Y
        # x = np.linspace(0, 2*np.pi, 100)
        # y = np.sin(x)

        # # Crear una figura y un eje
        # self.fig, self.ax = plt.subplots()

        # # Dibujar el gráfico de líneas
        # self.ax.plot(x, y)

        # # Crear un canvas y mostrar el gráfico en él
        # self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas)
        # self.canvas.draw()
        # self.canvas.get_tk_widget().grid(
        #     row=7, column=0, columnspan=5, pady=8, padx=8
        # )

        self.current_graph = LineGraph(self.master, row=7, column=0)
        self.voltage_graph = LineGraph(self.master, row=8, column=0)
        self.temperature_graph = LineGraph(self.master, row=9, column=0)
        self.humidity_graph = LineGraph(self.master, row=10, column=0)
