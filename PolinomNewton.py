import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

def divided_diff(x, y):
    n = len(x)
    coef = [[0] * n for _ in range(n)]
    for i in range(n):
        coef[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return [coef[i][i] for i in range(n)]

def newton_interpolasi(x, y, xi):
    coef = divided_diff(x, y)
    n = len(x)
    yi = []
    for xi_val in xi:
        term = coef[0]
        for k in range(1, n):
            prod = coef[k]
            for j in range(k):
                prod *= (xi_val - x[j])
            term += prod
        yi.append(term)
    return yi

def verify_interpolation_at_data_points(x, y):
    y_interpolated = newton_interpolasi(x, y, x)
    print("Verifikasi hasil interpolasi pada titik data asli:")
    for xi, yi, yi_interpolated in zip(x, y, y_interpolated):
        print(f"x = {xi}, y_asli = {yi}, y_interpolasi = {yi_interpolated}")

verify_interpolation_at_data_points(x, y)

x_values = [i for i in range(5, 41)]
y_values_newton = newton_interpolasi(x, y, x_values)

plt.plot(x, y, 'o', label='Data asli')
plt.plot(x_values, y_values_newton, '-', label='Interpolasi Newton')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.show()
