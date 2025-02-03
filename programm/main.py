import csv
import matplotlib.pyplot as plt

# CSV-Datei lesen
with open(r'C:\Users\steve\Documents\Programmieren\windDataAnalyse\data\test2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    x = []
    y = []
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
    plt.plot(x, y, marker="o")


# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('Zeit (s)')
plt.ylabel('Spannung (V)')
plt.title('Spannung über Zeit')

# Plot anzeigen
plt.show()