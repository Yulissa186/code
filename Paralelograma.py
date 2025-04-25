import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Definir los puntos A, B, C, D
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.array([1, 3, 3])
D = np.array([0, 2, 2])

# Definir los vértices del paralelogramo
vertices = np.array([A, B, C, D])

# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el paralelogramo conectando los puntos
verts = [[A, B, C, D]]
ax.add_collection3d(Poly3DCollection(verts, color='cyan', alpha=0.5, edgecolors='r'))

# Etiquetar los puntos
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='k')
for i, point in enumerate(['A', 'B', 'C', 'D']):
    ax.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], point, fontsize=12, color='blue')

# Establecer los límites de los ejes
ax.set_xlim([-1, 3])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title('Paralelogramo definido por A(1,1,1), B(2,2,2), C(1,3,3), D(0,2,2)')

# Mostrar la figura
plt.show()
