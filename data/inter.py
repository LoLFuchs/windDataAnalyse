import csv

def process_csv(input_file_path, output_file_path):
    # Liste zum Speichern der validen Werte
    valid_values = []
    
    # Datei öffnen und Zeilen durchgehen
    with open(input_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:
                # Überprüfen, ob es genug Spalten gibt und ob der Wert in der zweiten Spalte 0 ist
                if len(row) >= 2 and float(row[1]) != 0:
                    # Werte aus der zweiten Spalte extrahieren und prüfen, ob sie > 10 sind
                    value = float(row[1])
                    if value > 10:
                        valid_values.append(value)
            except ValueError:
                # Fehler beim Umwandeln der Werte vermeiden (z.B. falls nicht numerische Daten enthalten sind)
                continue
    
    # Berechnung des Durchschnitts, falls es gültige Werte gibt
    if valid_values:
        average = sum(valid_values) / len(valid_values)
        print(f"Durchschnitt der Werte größer als 10: {average}")
    else:
        print("Keine gültigen Werte gefunden, die größer als 10 sind.")
    
    # Schreibe die validen Werte in eine neue CSV-Datei
    with open(output_file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        # Schreibe die Header-Zeile
        csv_writer.writerow(["Index", "Wert"])
        
        # Schreibe die validen Werte mit aufsteigendem Index
        for index, value in enumerate(valid_values, start=1):
            csv_writer.writerow([index, value])
    
    print(f"Die validen Werte wurden in '{output_file_path}' gespeichert.")

# Beispielaufruf der Funktion mit einer CSV-Datei
input_file_path = 'Unwucht.csv'  # Pfad zur Eingabedatei anpassen
output_file_path = 'UnwuchtInter.csv'  # Pfad zur Ausgabedatei anpassen
process_csv(input_file_path, output_file_path)