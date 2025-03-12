from condicion import NumeroCondicion
from potencia import MetodoPotencia
from potencia_inverso import MetodoPotenciaInverso

class AnalisisDeRiesgo:
    def __init__(self):
        self.numero_condicion = NumeroCondicion(20)
        self.matriz_firma = self.numero_condicion.generar_matriz_aleatoria()
        self.potencia = MetodoPotencia(self.matriz_firma)
        self.potencia_inverso = MetodoPotenciaInverso(self.matriz_firma)
        
    def analizar_portafolio(self):
        """
        Realiza el análisis completo del portafolio, incluyendo el cálculo del número de condición,
        el autovalor dominante, el autovalor más pequeño y la visualización de la convergencia.
        """
        # 1. Cálculo del número de condición
        condicion = self.numero_condicion.obtener_condicion()
        print(f"Número de condición de la matriz de covarianza: {condicion}")
        if condicion > 1e6:
            print("Advertencia: El número de condición es alto. El portafolio puede ser muy sensible a cambios pequeños.")

        # 2. Método de Potencia para el autovalor dominante
        autovalor_dominante, autovector_dominante = self.potencia.calcular()
        print(f"Autovalor dominante: {autovalor_dominante}")
        print(f"Autovector dominante: {autovector_dominante}")
        self.potencia.graficar_convergencia()

        # 3. Método de Potencia Inverso para el autovalor más pequeño
        autovalor_pequeno, autovector_pequeno = self.potencia_inverso.calcular_autovalor()
        print(f"Autovalor más pequeño: {autovalor_pequeno}")
        print(f"Autovector asociado: {autovector_pequeno}")
        self.potencia_inverso.graficar_convergencia()

AnalisisDeRiesgo().analizar_portafolio()