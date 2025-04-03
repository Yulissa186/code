import numpy as np
import matplotlib.pyplot as plt

# Datos de las fuerzas
F1 = 140  # N
F2 = 60   # N
F3 = 160  # N (igual a F1 en este caso)

# Calcular el ángulo α a partir de la ecuación F2 = 2F1 * sin(α)
sin_alpha = F2 / (2 * F1)
alpha = np.arcsin(sin_alpha)
alpha_deg = np.degrees(alpha)  # Convertir a grados

print(f"El ángulo α es aproximadamente: {alpha_deg:.2f} grados")

# Calcular las componentes de las fuerzas
F1x = F1 * np.cos(alpha)
F1y = F1 * np.sin(alpha)

F3x = F3 * np.cos(alpha)  # F3 es igual a F1
F3y = F3 * np.sin(alpha)

# Graficar las fuerzas
plt.figure()
plt.quiver(0, 0, F1x, F1y, angles='xy', scale_units='xy', scale=1, color='r', label='F1')
plt.quiver(0, 0, 0, F2, angles='xy', scale_units='xy', scale=1, color='g', label='F2 (vertical)')
plt.quiver(0, 0, -F3x, F3y, angles='xy', scale_units='xy', scale=1, color='b', label='F3')

# Configurar los límites de los ejes
plt.xlim(-160, 160)
plt.ylim(0, 160)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)

# Etiquetas y título
plt.legend()
plt.xlabel('Componente X (N)')
plt.ylabel('Componente Y (N)')
plt.title(f'Diagrama de las fuerzas con α = {alpha_deg:.2f}°')

# Mostrar el gráfico
plt.show()
