import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
dia = int(input("Diameter: "))
if dia%2==0:
    dia+=1
rad = dia/2
def crater_matrix(r):
    d = int(2*r)
    var33 = (d)/3

    x_OD = (r**2)
    x_OD -= (var33)**2
    x_OD /= 2*var33

    new_r = x_OD + (d / 3)
    x0 = math.floor(d/2)
    y0 = x_OD
    z0 = math.floor(d/2)
    matrix = np.zeros((d,d))
    for z in range(0,d):
        for x in range(0,d):
            if ((new_r*new_r) - ((x-x0)*(x-x0)) - ((z-z0)*(z-z0)))>=0:
                y = y0 - math.sqrt((new_r*new_r) - ((x-x0)*(x-x0)) - ((z-z0)*(z-z0)))
                matrix[z][x] = y
            else:
                matrix[z][x] = 0
    for i in range(0,d):
        for j in range(0,d):
            if matrix[i][j]>0:
                matrix[i][j]=0
    return matrix

arr = crater_matrix(rad)
print(arr)
print(arr.shape)
print(np.min(arr))
print(dia/3)
print(arr[49][49])
X = np.linspace(0, dia, arr.shape[0])
Z = np.linspace(0, dia, arr.shape[1]) 
X, Z = np.meshgrid(X, Z)
Y = arr

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Z, Y, cmap='viridis')
fig.colorbar(surf)
ax.set_xlabel('X-axis')
ax.set_ylabel('Z-axis')
ax.set_zlabel('Y-axis')
def save_obj_file(filename, X, Y, Z):
    vertex_map = {}
    index = 1
    with open(filename, 'w') as obj_file:
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                if Y[i, j] != 0:  
                    obj_file.write(f"v {X[i, j]} {Y[i, j]} {Z[i, j]}\n")
                    vertex_map[(i, j)] = index
                    index += 1
        for i in range(X.shape[0] - 1):
            for j in range(X.shape[1] - 1):
                if (i, j) in vertex_map and (i, j + 1) in vertex_map and (i + 1, j) in vertex_map and (i + 1, j + 1) in vertex_map:
                    v1 = vertex_map[(i, j)]
                    v2 = vertex_map[(i, j + 1)]
                    v3 = vertex_map[(i + 1, j)]
                    v4 = vertex_map[(i + 1, j + 1)]
                    obj_file.write(f"f {v1} {v2} {v4} {v3}\n")
save_obj_file('circular_crater.obj', X, Y, Z)


