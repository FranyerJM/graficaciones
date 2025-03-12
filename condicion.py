import numpy as np
import matplotlib.pyplot as plt

class NumeroCondicion:
    def __init__(self, n):
        self.n = n
        self.tamanos = list(range(3, n+1))
        self.tamano_matriz = []
        self.condicion_matriz = []
    
    def generar_matriz_aleatoria(self):
        tamano = self.n
        matriz = np.random.randint(-20, 20, size=(tamano, tamano))
        print("Matriz generada:\n", matriz)
        return matriz
    
    def obtener_condicion(self):
        tamano = self.n
        matriz = self.generar_matriz_aleatoria()
        #matriz = np.array([[1, 3, 0], [4, 7, 2], [3, 4, 2]]) # det0
        det = np.linalg.det(matriz)
        if det != 0.0:
            nc = np.linalg.cond(matriz)
            self.tamano_matriz.append(tamano)
            self.condicion_matriz.append(nc)
            print(f"Número de condición: {nc}")
            return nc
        else:
            print(f"La matriz {matriz.shape[0]}x{matriz.shape[1]} es singular")
            return None
        
    def plot_time(self):
        """
        Grafica el número de condición en función del tamaño de la matriz.
        """
        if len(self.tamano_matriz) > 0:  # Verificar que hay datos para graficar
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            x = self.tamano_matriz  # Tamaños de las matrices
            y = self.condicion_matriz  # Números de condición
            z = np.zeros_like(x)  # Valores en el eje Z (0 para todos)

            ax.scatter(x, y, z, c='b', marker='o', s=100)  # Graficar puntos

            ax.set_xlabel('Tamaño de la matriz')
            ax.set_ylabel('Número de condición')
            ax.set_zlabel('Z')
            plt.title('Tamaño vs Condición')

            ax.view_init(elev=20, azim=30)  # Ajustar la vista del gráfico 3D
            plt.show()
        else:
            print("No hay datos para graficar: todas las matrices son singulares.")
    

def main():
    nxn = int(input("Ingrese tamaño de la matriz (n): "))
    ejercicio1 = NumeroCondicion(nxn)
    resultado = ejercicio1.obtener_condicion()

    # Gráfico NumeroCondicion
    def plot_time():
        if resultado is not None:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
            x = ejercicio1.tamano_matriz
            y = ejercicio1.condicion_matriz
            z = 0
            
            ax.scatter(x, y, z, c='b', marker='o', s=100)
            
            ax.set_xlabel('Tamaño de la matriz')
            ax.set_ylabel('Número de condición')
            ax.set_zlabel('Z')
            plt.title('Tamaño vs Condición')
            
            ax.view_init(elev=20, azim=30)
            
            plt.show()
        else:
            print("No se pudo graficar: matriz singular.")
    plot_time()

# if __name__ == "__main__":
#     main()