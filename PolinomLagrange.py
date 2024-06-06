x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

import matplotlib.pyplot as plt

def lagrange_interpolasi(x, y, xi):
    def L(k, xi):
        Lk = 1
        for i in range(len(x)):
            if i != k:
                Lk *= (xi - x[i]) / (x[k] - x[i])
        return Lk
    
    yi = []
    for xi in xi:
        yi.append(sum(y[k] * L(k, xi) for k in range(len(x))))
    return yi

x_values = [i for i in range(5, 41)]
y_values_lagrange = lagrange_interpolasi(x, y, x_values)

plt.plot(x, y, 'o', label='Data asli')
plt.plot(x_values, y_values_lagrange, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.show()

