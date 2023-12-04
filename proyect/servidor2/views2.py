import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from server import run_server
import threading
import valores

# Variables globales para las etiquetas
global temp_label, hum_label, amps_label, voltage_label, master

# Variables globales para las graficas
global temp_data, hum_data, amps_data, voltage_data
temp_data = []
hum_data = []
amps_data = []
voltage_data = []


def create_interface():
    # Variables globales para las etiquetas
    global temp_label, hum_label, amps_label, voltage_label, master

    # Variables globales para las graficas
    global temp_data, hum_data, amps_data, voltage_data
    global temp_graph, hum_graph, amps_graph, voltage_graph
    global canvas_temp, canvas_hum, canvas_amps, canvas_voltage

    master = tk.Tk()
    master.title('Interfaz')

    color = "#FB0909"

    # Crear una figura y un eje
    fig_temp, temp_graph = plt.subplots(figsize=(5, 3))
    fig_temp.suptitle('Temperatura')

    fig_hum, hum_graph = plt.subplots(figsize=(5, 3))
    fig_hum.suptitle('Humedad')

    fig_amps, amps_graph = plt.subplots(figsize=(5, 3))
    fig_amps.suptitle('Amperios')

    fig_voltage, voltage_graph = plt.subplots(figsize=(5, 3))
    fig_voltage.suptitle('Voltaje')
    # ...

    # Crear un canvas
    canvas_temp = FigureCanvasTkAgg(fig_temp, master=master)
    canvas_temp.get_tk_widget().grid(row=9, rowspan=2, column=0, columnspan=4)

    canvas_hum = FigureCanvasTkAgg(fig_hum, master=master)
    canvas_hum.get_tk_widget().grid(row=9, rowspan=2, column=5, columnspan=4)

    canvas_amps = FigureCanvasTkAgg(fig_amps, master=master)
    canvas_amps.get_tk_widget().grid(row=14, rowspan=2, column=0, columnspan=4)

    canvas_voltage = FigureCanvasTkAgg(fig_voltage, master=master)
    canvas_voltage.get_tk_widget().grid(
        row=14, rowspan=2, column=5, columnspan=4
    )

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
    hum_label.grid(row=2, column=6, sticky="w", pady=2, padx=2)

    amps_label = tk.Label(master, text="Amperios:")
    amps_label.grid(row=5, column=3, sticky="w", pady=2, padx=2)

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

    update_labels()

    # Inicia el bucle principal de Tkinter
    master.mainloop()


# Inicia la actualización de la interfaz
def update_labels():
    # Actualizar las etiquetas
    temp_label.config(text=f"Temperatura: {valores.temperatura}")
    hum_label.config(text=f"Humedad: {valores.humedad}")
    amps_label.config(text=f"Amperios: {valores.amps}")
    voltage_label.config(text=f"Voltaje: {valores.voltage}")

    # Actualizar nuevos valores a las listas
    temp_data.append(valores.temperatura)
    hum_data.append(valores.humedad)
    amps_data.append(valores.amps)
    voltage_data.append(valores.voltage)

    # Actualizar las graficas
    temp_graph.clear()
    temp_graph.plot(temp_data, color="red")
    canvas_temp.draw()

    hum_graph.clear()
    hum_graph.plot(hum_data, color="blue")
    canvas_hum.draw()

    amps_graph.clear()
    amps_graph.plot(amps_data, color="green")
    canvas_amps.draw()

    voltage_graph.clear()
    voltage_graph.plot(voltage_data, color="orange")
    canvas_voltage.draw()

    master.after(1000, update_labels)


if __name__ == "__main__":
    # Iniciar el servidor en un hilo separado
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    create_interface()
    # run_server()
