import serial, time
from collections import deque

def maintain_n_values(n):
    # Deque for maintaining the last n values
    values = deque(maxlen=n)
    
    def add_value(new_value):
        # Append the new value and the deque automatically discards the oldest if necessary
        values.append(new_value)
        return list(values)  # Return the current list of n values

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

def readserial(comport, baudrate, n):

    start = time.time_ns()
    f = open("../data/Foehn3.csv", "w")
    f.write("Zeit in ms, Spannung in Einheitslos\n")
    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                print(data)
                slope = int(data) - moving_average(add_value(int(data)))
                if abs(slope) > 150:
                    print("ANOMALIE!!!")
                    f.write("ANOMALIE!!!\n")
                line = "" + str(time.time_ns() - start) + "," + data + "\n"
                f.write(line)
        except(UnicodeDecodeError):
            print("Failed")

    f.close()

n = 100
add_value = maintain_n_values(n)

readserial("/dev/ttyACM0", 9600, n)