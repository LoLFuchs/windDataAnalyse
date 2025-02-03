import csv
import matplotlib.pyplot as plt

# CSV-Datei lesen
with open(r'C:\Users\steve\Documents\Programmieren\windDataAnalyse\data\Foehn2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    time = []
    voltage = []
    for row in reader:
        time.append(float(row[0]))
        voltage.append(float(row[1]))
    plt.plot(time, voltage, marker="o")


voltageMittelwert = 0
for x in voltage:
    voltageMittelwert += x
    
voltageMittelwert = voltageMittelwert / len(voltage)
print(f"voltageMittelwert: {voltageMittelwert}")

with open(r'C:\Users\steve\Documents\Programmieren\windDataAnalyse\data\Korrekt1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    i = 0
    for row in reader:
        i += 1
        
        
        if i == 10:
            print(2)


# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('Zeit (ms)')
plt.ylabel('Spannung (V)')
plt.title('Spannung über Zeit')

# Plot anzeigen
plt.show()