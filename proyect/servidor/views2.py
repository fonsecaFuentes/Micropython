import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Etiquetas como variables globales
global temp_label, hum_label, amps_label, voltage_label


def create_interface():
    global temp_label, hum_label, amps_label, voltage_label
    master = tk.Tk()
    master.title('Interfaz')

    color = "#FB0909"

    # Crear una figura y un eje
    fig, ax = plt.subplots(figsize=(4, 2.5))

    # Crear un canvas
    amps_graph = FigureCanvasTkAgg(fig, master=master)
    amps_graph.get_tk_widget().grid(row=9, rowspan=2, column=0, columnspan=4)

    voltage_graph = FigureCanvasTkAgg(fig, master=master)
    voltage_graph.get_tk_widget().grid(
        row=14, rowspan=2, column=0, columnspan=4
    )

    temp_graph = FigureCanvasTkAgg(fig, master=master)
    temp_graph.get_tk_widget().grid(row=9, rowspan=2, column=5, columnspan=4)

    hum_graph = FigureCanvasTkAgg(fig, master=master)
    hum_graph.get_tk_widget().grid(row=14, rowspan=2, column=5, columnspan=4)

    # Crear Layout
    layout_amps = tk.Label(
        master,
        text="Temperatura y Humedad",
        bg="DarkOrchid3",
        fg="thistle1",
        width=40
    )
    layout_amps.grid(
        row=0,
        rowspan=2,
        column=0,
        columnspan=9,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    layout_voltage = tk.Label(
        master,
        text="Voltaje y Amperios",
        bg="DarkOrchid3",
        fg="thistle1",
        width=40
    )
    layout_voltage.grid(
        row=3,
        rowspan=2,
        column=0,
        columnspan=9,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    layout_amps_graph = tk.Label(
        master,
        text="Temperatura y Humedad Gráfica",
        bg="DarkOrchid3",
        fg="thistle1",
        width=40
    )

    layout_amps_graph.grid(
        row=7,
        rowspan=2,
        column=0,
        columnspan=9,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    layout_voltage_graph = tk.Label(
        master,
        text="Voltaje y Amperios Gráfica",
        bg="DarkOrchid3",
        fg="thistle1",
        width=40
    )
    layout_voltage_graph.grid(
        row=12,
        rowspan=2,
        column=0,
        columnspan=9,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    layout_relay = tk.Label(
        master,
        text="Relay",
        bg="DarkOrchid3",
        fg="thistle1",
        width=40
    )
    layout_relay.grid(
        row=17,
        rowspan=2,
        column=0,
        columnspan=9,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    relay_indicator1 = tk.Label(
        master,
        text="",
        bg=color,
        fg="#000000",
        width=15
    )
    relay_indicator1.grid(
        row=22,
        column=0,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    relay_indicator1 = tk.Label(
        master,
        text="",
        bg=color,
        fg="#000000",
        width=15
    )
    relay_indicator1.grid(
        row=22,
        column=2,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    relay_indicator3 = tk.Label(
        master,
        text="",
        bg=color,
        fg="#000000",
        width=15
    )
    relay_indicator3.grid(
        row=22,
        column=6,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    relay_indicator3 = tk.Label(
        master,
        text="",
        bg=color,
        fg="#000000",
        width=15
    )
    relay_indicator3.grid(
        row=22,
        column=8,
        sticky="w" + "e",
        pady=8,
        padx=8
    )

    # Crear una etiqueta
    temp_label = tk.Label(master, text="Temperatura:")
    temp_label.grid(row=2, column=3, sticky="w", pady=2, padx=2)

    hum_label = tk.Label(master, text="Humedad:")
    hum_label.grid(row=5, column=3, sticky="w", pady=2, padx=2)

    amps_label = tk.Label(master, text="Amperios:")
    amps_label.grid(row=2, column=6, sticky="w", pady=2, padx=2)

    voltage_label = tk.Label(master, text="Voltaje:")
    voltage_label.grid(row=5, column=6, sticky="w", pady=2, padx=2)

    # Crear un botón
    boton_relay1 = tk.Button(master, text="ENCENDER 1")
    boton_relay1.grid(row=20, column=0, sticky="nsew", pady=8, padx=8)

    boton_relay2 = tk.Button(master, text="ENCENDER 2")
    boton_relay2.grid(row=20, column=2, sticky="nsew", pady=8, padx=8)

    boton_relay3 = tk.Button(master, text="ENCENDER 3")
    boton_relay3.grid(row=20, column=6, sticky="nsew", pady=8, padx=8)

    boton_relay4 = tk.Button(master, text="ENCENDER 4")
    boton_relay4.grid(row=20, column=8, sticky="nsew", pady=8, padx=8)

    # Inicia el bucle principal de Tkinter
    master.mainloop()


def get_labels():
    return temp_label, hum_label, amps_label, voltage_label

# # Crea la interfaz gráfica
# create_interface()
