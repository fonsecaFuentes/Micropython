import tkinter as tk
from tkinter import StringVar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from server import run_server
import threading


def create_interface():
    master = tk.Tk()
    master.title('Interfaz')

    color = "#FB0909"

    # Variables para amperios y voltaje
    amps_value = StringVar()
    voltage_value = StringVar()
    temp_value = StringVar()
    hum_value = StringVar()

    # Crear una figura y un eje
    fig, ax = plt.subplots(figsize=(4, 2.5))

    # Crear un canvas
    amps_graph = FigureCanvasTkAgg(fig, master=master)
    amps_graph.get_tk_widget().grid(row=9, rowspan=2, column=0, columnspan=4)

    voltage_graph = FigureCanvasTkAgg(fig, master=master)
    voltage_graph.get_tk_widget().grid(row=14, rowspan=2, column=0, columnspan=4)

    temp_graph = FigureCanvasTkAgg(fig, master=master)
    temp_graph.get_tk_widget().grid(row=9, rowspan=2, column=5, columnspan=4)

    hum_graph = FigureCanvasTkAgg(fig, master=master)
    hum_graph.get_tk_widget().grid(row=14, rowspan=2, column=5, columnspan=4)

    # Crear Layout
    layout_amps = tk.Label(
        master,
        text="Amperios",
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
        text="Voltaje",
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
        text="Amperios Gráfica",
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
        text="Voltaje Gráfica",
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
    amps_label = tk.Label(master, text="Amperios:")
    amps_label.grid(row=2, column=4, sticky="w", pady=2, padx=2)

    voltage_label = tk.Label(master, text="Voltaje:")
    voltage_label.grid(row=5, column=4, sticky="w", pady=2, padx=2)

    # Crear un botón
    boton_relay1 = tk.Button(master, text="ENCENDER 1")
    boton_relay1.grid(row=20, column=0, sticky="nsew", pady=8, padx=8)

    boton_relay2 = tk.Button(master, text="ENCENDER 2")
    boton_relay2.grid(row=20, column=2, sticky="nsew", pady=8, padx=8)

    boton_relay3 = tk.Button(master, text="ENCENDER 3")
    boton_relay3.grid(row=20, column=6, sticky="nsew", pady=8, padx=8)

    boton_relay4 = tk.Button(master, text="ENCENDER 4")
    boton_relay4.grid(row=20, column=8, sticky="nsew", pady=8, padx=8)

    # Iniciar el servidor en un hilo separado
    server_hilo = threading.Thread(target=run_server)
    server_hilo.start()

    # Inicia el bucle principal de Tkinter
    master.mainloop()


def actualizar_valores():
    global temperatura_data  # Accede a la variable global
    global bar  # Accede a la variable global

    # Accede a las variables de instancia de la clase S
    temperatura = S.temperatura
    humedad = S.humedad
    lux = S.lux

    # Actualiza las etiquetas con los valores de S
    etiqueta_temperatura.config(text=f"Temperatura: {temperatura}")
    etiqueta_humedad.config(text=f"Humedad: {humedad}")
    etiqueta_lux.config(text=f"Lux: {lux}")

    # Actualiza los datos de temperatura para el gráfico
    temperatura_data[0] = temperatura

    if bar is not None:  # Verifica si bar no es None antes de acceder a él
        bar[0].set_height(temperatura_data[0])
        canvas.draw()

    # Programa una llamada a esta función nuevamente después de un tiempo
    ventana.after(1000, actualizar_valores)


# Crea la interfaz gráfica
create_interface()
