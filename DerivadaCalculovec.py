import numpy as np
import matplotlib.pyplot as plt

# Función para graficar la curva y la línea tangente
def plot_curve_and_tangent(X_func, Y_func, X_prime_func, Y_prime_func, t_value, t_range, title):
    t = np.linspace(*t_range, 100)
    X = X_func(t)
    Y = Y_func(t)
    
    # Evaluamos en el punto t_value
    x_t = X_func(t_value)
    y_t = Y_func(t_value)
    x_prime = X_prime_func(t_value)
    y_prime = Y_prime_func(t_value)
    
    # Pendiente de la tangente
    slope = y_prime / x_prime
    
    # Ecuación de la línea tangente
    tangent_line = slope * (t - x_t) + y_t
    
    # Graficar
    plt.figure(figsize=(8, 6))
    plt.plot(X, Y, label='Curva Paramétrica', color='blue')
    plt.plot(t, tangent_line, label='Línea Tangente', color='red', linestyle='--')
    plt.scatter(x_t, y_t, color='green', label='Punto de Tangencia')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.axis('equal')
    plt.show()

# a) X(t) = e^t, Y(t) = cos(t), t = π/4
plot_curve_and_tangent(
    lambda t: np.exp(t), 
    lambda t: np.cos(t), 
    lambda t: np.exp(t), 
    lambda t: -np.sin(t), 
    np.pi / 4, 
    (0, 3), 
    'Curva Paramétrica a) X(t) = e^t, Y(t) = cos(t)'
)

# b) X(t) = 3t^2, Y(t) = t^3, t = 2
plot_curve_and_tangent(
    lambda t: 3 * t**2, 
    lambda t: t**3, 
    lambda t: 6 * t, 
    lambda t: 3 * t**2, 
    2, 
    (0, 10), 
    'Curva Paramétrica b) X(t) = 3t^2, Y(t) = t^3'
)

# c) X(t) = t*sin(t), Y(t) = 4t, t = π/2
plot_curve_and_tangent(
    lambda t: t * np.sin(t), 
    lambda t: 4 * t, 
    lambda t: np.sin(t) + t * np.cos(t), 
    lambda t: 4, 
    np.pi / 2, 
    (0, 5), 
    'Curva Paramétrica c) X(t) = t*sin(t), Y(t) = 4t'
)

# d) X(t) = t^2, Y(t) = e^(2t), t = 1
plot_curve_and_tangent(
    lambda t: t**2, 
    lambda t: np.exp(2 * t), 
    lambda t: 2 * t, 
    lambda t: 2 * np.exp(2 * t), 
    1, 
    (0, 3), 
    'Curva Paramétrica d) X(t) = t^2, Y(t) = e^(2t)'
)
