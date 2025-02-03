import serial, time

def readserial(comport, baudrate):

    start = time.time_ns()
    f = open("Foehn1.csv", "w")
    f.write("Zeit in ms, Spannung in Einheitslos\n")
    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                print(data)
                line = "" + str(time.time_ns() - start) + "," + data + "\n"
                f.write(line)
        except(UnicodeDecodeError):
            print("Failed")

    f.close()

readserial("/dev/ttyACM0", 115200)