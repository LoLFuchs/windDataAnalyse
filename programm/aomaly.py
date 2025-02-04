import serial
import time
import threading
import matplotlib.pyplot as plt
from collections import deque
from queue import Queue

# Function to handle multiple values
def maintain_multiple_values(n, keys):
    values_dict = {key: deque(maxlen=n) for key in keys}
    
    def add_value(key, new_value=None):
        if key in values_dict:
            if new_value is None:
                return list(values_dict[key])
            else:
                values_dict[key].append(new_value)
                return list(values_dict[key])
        else:
            raise ValueError(f"Key '{key}' not found!")
    
    return add_value

# Moving average function
def moving_average(values):
    if not values:
        raise ValueError("The list cannot be empty.")
    return sum(values) / len(values)

# Serial data reading in a thread
def readserial(comport, baudrate, n, data_queue):
    start = time.time_ns()
    ser = serial.Serial(comport, baudrate, timeout=0.1)
    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                data_value = int(data)
                time_value = time.time_ns() - start
                data_queue.put((time_value, data_value))  # Send data to main thread
        except UnicodeDecodeError:
            print("Failed to read data")

# Initialize the main values handler
n = 100
keys = ['time', 'voltage']
add_value = maintain_multiple_values(n, keys)

# Initialize the plot
plt.ion()
fig, ax = plt.subplots()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
linePlot, = ax.plot([], [], marker="o")

# Create a queue for thread communication
data_queue = Queue()

# Start the serial reading thread
thread1 = threading.Thread(target=readserial, args=("/dev/ttyACM0", 9600, n, data_queue))
thread1.start()

# Main loop for updating the plot
while True:
    # Check if there's new data from the serial thread
    if not data_queue.empty():
        time_value, voltage_value = data_queue.get()
        
        # Update the values in the dictionary
        add_value("time", time_value)
        add_value("voltage", voltage_value)

        # Update the plot with new data
        linePlot.set_xdata(add_value("time", None))  # Get time values
        linePlot.set_ydata(add_value("voltage", None))  # Get voltage values
        
        # Adjust axis limits based on the new data
        ax.relim()
        ax.autoscale_view()

        # Redraw the plot
        fig.canvas.draw()
        fig.canvas.flush_events()
    
    # Pause to update the plot
    plt.pause(0.1)
