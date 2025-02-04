import csv
import matplotlib.pyplot as plt
import time
from collections import deque
import threading

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

def moving_average(values):
    """
    Berechnet das durchschnittliche Mittel aller Werte in der Liste.
    
    :param values: Eine Liste von Zahlen, aus denen das durchschnittliche Mittel berechnet werden soll.
    :return: Der durchschnittliche Mittelwert aller Werte in der Liste.
    """
    if not values:
        raise ValueError("Die Liste darf nicht leer sein.")
    
    return sum(values) / len(values)

n = 10
voltageInter = maintain_multiple_values(n, "voltageInter")
curNum = 0
timer = 0

# CSV-Datei lesen
f = open("../data/UnwuchtInterpolation.csv", "w")
f.write("Zeit in ms, Spannung in Einheitslos\n")
with open(r'../data/Unwucht.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    time = []
    voltage = []
    for row in reader:
        if float(row[1]) > 0:
            time.append(float(row[0]))
            voltage.append(float(row[1]))
            voltageInter("voltageInter", float(row[1]))
            curNum += 1

        if curNum == n:
            f.write("" + str(timer) + "," + str(moving_average(voltageInter("voltageInter"))) + "\n")
            timer += 1

    plt.plot(time, voltage, marker="o")

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('Zeit (ms)')
plt.ylabel('Spannung (V)')
plt.title('Spannung über Zeit')

# Plot anzeigen
plt.show()