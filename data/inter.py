import csv

def process_csv(input_file_path, output_file_path):
    # Liste zum Speichern der validen Werte
    valid_values = []
    counter = 0
    index = 0
    num = 100
    
    # Datei öffnen und Zeilen durchgehen
    with open(input_file_path, mode='r') as file:
        with open(output_file_path, mode='w') as fileOut:
            csv_writer = csv.writer(fileOut)
            csv_writer.writerow(["Zeit", "Voltage"])
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try:
                    # Überprüfen, ob es genug Spalten gibt und ob der Wert in der zweiten Spalte 0 ist
                    if len(row) >= 2 and float(row[1]) != 0:
                        # Werte aus der zweiten Spalte extrahieren und prüfen, ob sie > 10 sind
                        value = float(row[1])
                        valid_values.append(value)
                        counter += 1

                    if counter == num:
                        average = sum(valid_values) / len(valid_values)
                        csv_writer.writerow([index, average])
                        index += 1
                        counter = 0
                        valid_values = []
                except ValueError:
                    # Fehler beim Umwandeln der Werte vermeiden (z.B. falls nicht numerische Daten enthalten sind)
                    continue

# Beispielaufruf der Funktion mit einer CSV-Datei
input_file_path = 'Schraeg45.csv'  # Pfad zur Eingabedatei anpassen
output_file_path = 'Schraeg45Inter.csv'  # Pfad zur Ausgabedatei anpassen
process_csv(input_file_path, output_file_path)