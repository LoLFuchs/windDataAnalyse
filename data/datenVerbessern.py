import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def sin_fn(x, A,B,C,D,E,F):
    return A*x**2 + B*x *  C* np.sin(D*x**2 +E*x +F)



x = []
y = []

def to_array(filename):
    x = []
    y = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    return (x,y)


norm = to_array("Normal.csv")
norm = norm[1][10000:-10000]
x_fine_norm = np.linspace(0, len(norm), 100)
#koef_norm = np.polyfit(norm[0], norm[1],2)
#poly_norm = np.poly1d(koef_norm)
#y_poly_norm = poly_norm(x_fine_norm)

umwucht = to_array("Unwucht.csv")
umwucht = umwucht[1][1000:-1000]
x_fine_umwucht = np.linspace(0, len(norm), 100)
umwucht_sin_param = curve_fit(sin_fn,  len(umwucht), umwucht)
y_sin_umwucht = sin_fn(x_fine_umwucht, umwucht_sin_param[0], umwucht_sin_param[1], umwucht_sin_param[2], umwucht_sin_param[3], umwucht_sin_param[4], umwucht_sin_param[5])
#x_umwucht = np.linspace(min(umwucht[0]), max(umwucht[1]), 100)
#koef_umwucht = np.polyfit(umwucht[0], umwucht[1], 2)
#poly_umwucht = np.poly1d(koef_umwucht)
#y_poly_umwucht = poly_umwucht(x_umwucht)

norm_sin_param, _ = curve_fit(sin_fn, len(norm), norm)
y_sin_norm = sin_fn(x_fine_norm, norm_sin_param[0], norm_sin_param[1], norm_sin_param[2], norm_sin_param[3], norm_sin_param[4], norm_sin_param[5])


#y_fine = np.interp(x_fine, x, y, 100)

plt.scatter(x, y, color="red", label="Messung")
plt.plot(x_fine_norm, y_sin_norm, color="green", label="sin_norm")

#plt.plot(x_fine_norm, y_poly_norm, color="blue", label="Interpolate")
plt.plot(x_fine_umwucht, y_sin_umwucht, color="red", label="Umwucht")
plt.title("Normalbetrieb")
plt.xlabel("t")
plt.ylabel("U(t)")
#plt.ylim(0,100)
plt.show()