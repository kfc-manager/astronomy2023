import matplotlib.pyplot as plt
import numpy as np

teff = [52500, 44500, 41000, 35800, 30000, 18700, 15400, 11900, 9500, 8700, 8200, 7600, 7200, 6900, 6400, 6200, 6000, 5800, 5700, 5600, 5300, 4900, 4400, 4100, 3800, 3600, 3200, 3100]
mv = [-6.0, -5.7, -5.5, -4.9, -4.0, -1.6, -1.2, -0.2, 0.6, 1.5, 1.9, 2.4, 2.7, 3.6, 3.5, 4.0, 4.4, 4.7, 5.1, 5.5, 5.9, 6.4, 7.4, 8.1, 8.8, 9.9, 12.3, 13.5]
bc = [-4.751, -4.40, -3.93, -3.54, -3.16, -1.94, -1.46, -0.80, -0.30, -0.17, -0.15, -0.10, -0.09, -0.11, -0.14, -0.16, -0.18, -0.20, -0.21, -0.40, -0.31, -0.42, -0.72, -1.01, -1.38, -1.89, -2.73, -3.21]
mbol = 4.74
sigma = 5.67e-8


def st_boltzmann(teff, r):
    return 4 * np.pi * r**2 * sigma * teff**4

def calc_mv(l, l_circ, bc):
    return mbol - 2.5 * np.log(l / l_circ) - bc

plt.figure(figsize=(8,6))
plt.plot(list(map(lambda x: np.log(x), teff)), mv, marker='o', color='blue', alpha=0.7, label="base")
plt.plot(list(map(lambda x: np.log(x), teff)), list(map(lambda x, y: calc_mv(st_boltzmann(x, 0.1), st_boltzmann(x, 10.0), y), teff, bc)), marker='o', color='red', alpha=0.7, label="r = 0.1")
plt.plot(list(map(lambda x: np.log(x), teff)), list(map(lambda x, y: calc_mv(st_boltzmann(x, 1.0), st_boltzmann(x, 10.0), y), teff, bc)), marker='o', color='green', alpha=0.7, label="r = 1.0")
plt.title('Hertzsprung-Russell Diagram')
plt.xlabel('log (Effective Temperature)')
plt.ylabel('Absolute Visual Magnitude')

plt.gca().invert_yaxis()  # Invert y-axis for HR diagram convention

plt.legend()
plt.grid(True)
plt.show()
