import serial, time
from collections import deque
import matplotlib
import threading
matplotlib.use('TkAgg')  # oder 'Qt5Agg' oder ein anderes interaktives Backend

import matplotlib.pyplot as plt


def maintain_multiple_values(n, keys):
    # Ein Dictionary für mehrere Deques
    values_dict = {key: deque(maxlen=n) for key in keys}
    
    def add_value(key, new_value=None):
        """
        Fügt den neuen Wert zum entsprechenden Deque hinzu und gibt das Array für den Schlüssel zurück.
        
        :param key: Der Schlüssel (z.B. 'time' oder 'voltage')
        :param new_value: Der neue Wert, der dem Array hinzugefügt werden soll.
        :return: Das aktuelle Array (Liste) für den angegebenen Schlüssel.
        """
        if key in values_dict:
            if new_value == None:
                return list(values_dict)
            else:
                values_dict[key].append(new_value)
                return list(values_dict[key])  # Gibt das aktuelle Array (Liste) zurück
        else:
            raise ValueError(f"Key '{key}' nicht gefunden!")
    
    return add_value

numValues = 1000
time_value = maintain_multiple_values(numValues, "time")
voltage_value = maintain_multiple_values(numValues, "voltage")

def moving_average(values):
    """
    Berechnet das durchschnittliche Mittel aller Werte in der Liste.
    
    :param values: Eine Liste von Zahlen, aus denen das durchschnittliche Mittel berechnet werden soll.
    :return: Der durchschnittliche Mittelwert aller Werte in der Liste.
    """
    if not values:
        raise ValueError("Die Liste darf nicht leer sein.")
    
    return sum(values) / len(values)

def readserial(comport, baudrate, n, linePlot, ax):

    start = time.time_ns()
    f = open("../data/Unwucht.csv", "w")
    f.write("Zeit in ms, Spannung in Einheitslos\n")
    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    last_update = start

    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                print(data)
                slope = int(data) - moving_average(add_value("add", int(data)))
                if abs(slope) > 50:
                    print("ANOMALIE!!!")
                    # f.write("ANOMALIE!!!\n")
                line = "" + str(time.time_ns() - start) + "," + data + "\n"
                f.write(line)

        except(UnicodeDecodeError):
            print("Failed")

n = 100
keys = ['add', 'time', 'voltage']
add_value = maintain_multiple_values(n, keys)


plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()

# Set axis labels
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')

# Setting a limit for the x and y axis (adjust this as per your data)
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

# Create a line plot (initially empty)
linePlot, = ax.plot([], [], marker="o")

thread1 = threading.Thread(target=readserial, args=("/dev/ttyACM0", 9600, n, linePlot, ax,))
thread1.start()

while True:
    linePlot.set_xdata(add_value("time", time.time_ns() - start))
    linePlot.set_ydata(add_value("voltage", int(data)))
    
    # Automatically adjust the axis limits
    ax.relim()  # Recalculate limits based on the new data
    ax.autoscale_view()  # Adjust the axis to fit the new data

    # Redraw the plot
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    # Pause to update the plot (time in seconds)
    plt.pause(0.1)