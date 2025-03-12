import numpy as np
import matplotlib.pyplot as plt

class MetodoPotencia:
    def __init__(self, matriz, max_iter=300, tolerancia=1e-8):
        """
        Inicializa la clase con la matriz, el número máximo de iteraciones y la tolerancia.
        """
        self.matriz = matriz
        self.max_iter = max_iter
        self.tolerancia = tolerancia
        self.n = matriz.shape[0]
        self.vector_actual = np.random.randint(-5, 6, size=self.n)  # Vector inicial aleatorio
        print("Vector inicial utilizado:\n", self.vector_actual)
        self.vector_actual = self.vector_actual / np.linalg.norm(self.vector_actual)  # Normalización
        self.autovalor_hist = []  # Historial de autovalores
        self.autovector_hist = []  # Historial de autovectores

    def calcular(self):
        """
        Implementa el método de potencia para calcular el autovalor dominante y su autovector asociado.
        """
        for i in range(self.max_iter):
            nuevo_vector = self.matriz @ self.vector_actual  # Multiplicación matriz-vector
            autovalor_aprox = self.vector_actual @ nuevo_vector  # Aproximación del autovalor

            self.autovalor_hist.append(autovalor_aprox)  # Guardar autovalor en el historial
            if np.linalg.norm(nuevo_vector) == 0:  # Evitar división por cero
                return 0, self.vector_actual
            self.vector_actual = nuevo_vector / np.linalg.norm(nuevo_vector)  # Normalizar nuevo vector
            self.autovector_hist.append(self.vector_actual.copy())  # Guardar autovector en el historial

            # Verificar convergencia
            if len(self.autovalor_hist) > 1:
                dif = abs(self.autovalor_hist[-1] - self.autovalor_hist[-2])
                if dif < self.tolerancia:
                    print(f"Convergencia alcanzada en {i + 1} iteraciones")
                    break

        return autovalor_aprox, self.vector_actual

    def graficar_convergencia(self):
        """
        Grafica la convergencia del autovalor y las componentes del autovector.
        """
        plt.figure(figsize=(12, 5))

        # Gráfico del autovalor
        plt.subplot(1, 2, 1)
        plt.plot(self.autovalor_hist, 'o-', markersize=4)
        plt.xlabel('N Iteración')
        plt.ylabel('Autovalor estimado')
        plt.title('Convergencia del Autovalor Dominante')
        plt.grid(True)

        plt.subplot(1, 2, 2)
        autovector_hist = np.array(self.autovector_hist)
        for i in range(autovector_hist.shape[1]):
            plt.plot(autovector_hist[:, i], 'o--', markersize=4, label=f'Componente {i + 1}')
        plt.xlabel("N Iteraciones")
        plt.ylabel('Componentes del Autovector')
        plt.title('Convergencia del Autovector')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()
