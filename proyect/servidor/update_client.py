from views2 import temp_label, hum_label, amps_label, voltage_label, master


def update_labels(amps, voltage, temp, hum):
    # Actualiza las etiquetas con los valores de S
    temp_label.config(text=f"Temperatura: {temp}")
    hum_label.config(text=f"Humedad: {hum}")
    amps_label.config(text=f"Amperios: {amps}")
    voltage_label.config(text=f"Voltaje: {voltage}")

    # Llamada a esta función nuevamente después de un tiempo
    master.after(1000, lambda: update_labels(
        master, temp_label, hum_label, amps_label, voltage_label)
    )
