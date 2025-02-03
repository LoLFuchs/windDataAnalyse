import csv

import matplotlib.pyplot as plt

# CSV-Datei lesen
with open('/c:/Users/steve/Documents/Programmieren/windDataAnalyse/programm/data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Überspringe die Kopfzeile
    zeit = []
    spannung = []
    for row in reader:
        zeit.append(int(row[0]))
        spannung.append(float(row[1].replace(',', '.')))

# Plot erstellen
plt.plot(zeit, spannung, marker='o')

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('Zeit (s)')
plt.ylabel('Spannung (V)')
plt.title('Spannung über Zeit')

# Plot anzeigen
plt.show()