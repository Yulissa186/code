import numpy as np
import matplotlib.pyplot as plt

# Función para graficar figuras paramétricas
def plot_parametric_curve(X_func, Y_func, t_range, title):
    t = np.linspace(*t_range, 400)
    X = X_func(t)
    Y = Y_func(t)

    plt.figure(figsize=(8, 6))
    plt.plot(X, Y)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid()
    plt.axis('equal')
    plt.show()

# 1. Circunferencia
r = 1
plot_parametric_curve(
    lambda t: r * np.cos(t),
    lambda t: r * np.sin(t),
    (0, 2 * np.pi),
    'Circunferencia'
)

# 2. Cicloide
r = 1
plot_parametric_curve(
    lambda t: r * (t - np.sin(t)),
    lambda t: r * (1 - np.cos(t)),
    (0, 2 * np.pi),
    'Cicloide'
)

# 3. Hipocicloide
r = 1
plot_parametric_curve(
    lambda t: r * (2 * np.cos(t) - np.cos(2 * t)),
    lambda t: r * (2 * np.sin(t) - np.sin(2 * t)),
    (0, 2 * np.pi),
    'Hipocicloide'
)

# 4. Astroide
a = 1
plot_parametric_curve(
    lambda t: a * np.cos(t)**3,
    lambda t: a * np.sin(t)**3,
    (0, 2 * np.pi),
    'Astroide'
)

# 5. Lemoscata
a = 1
plot_parametric_curve(
    lambda t: a * np.sin(t) * np.cos(t),
    lambda t: a * (np.sin(t)**2 - np.cos(t)**2),
    (0, 2 * np.pi),
    'Lemoscata'
)

# 6. Cardioide
a = 1
plot_parametric_curve(
    lambda t: a * (1 - np.cos(t)) * np.cos(t),
    lambda t: a * (1 - np.cos(t)) * np.sin(t),
    (0, 2 * np.pi),
    'Cardioide'
)
