from PolinomLagrange import lagrange_interpolasi
from PolinomNewton import newton_interpolasi
import matplotlib.pyplot as plt

def test_interpolation():
    x = [5, 10, 15, 20, 25, 30, 35, 40]
    y = [40, 30, 25, 40, 18, 20, 22, 15]

    xi_test = [7, 12, 17, 22, 27, 32, 37]

    y_lagrange_test = lagrange_interpolasi(x, y, xi_test)
    print("Hasil interpolasi Lagrange pada xi_test:")
    for xi, yi in zip(xi_test, y_lagrange_test):
        print(f"x = {xi}, y = {yi}")

    y_newton_test = newton_interpolasi(x, y, xi_test)
    print("Hasil interpolasi Newton pada xi_test:")
    for xi, yi in zip(xi_test, y_newton_test):
        print(f"x = {xi}, y = {yi}")

test_interpolation()
