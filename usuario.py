#Fabian Vargas
from tarjetausuario import TarjetCredito
import tarjetausuario

class Usuario:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def agregar_tarjeta(self, tarjeta):
        """Agrega una tarjeta de crédito al usuario"""
        self.tarjetas.append(tarjeta)
        print(f"Tarjeta añadida por el usuario: {self.nombre}. ahora tiene {len(self.tarjetas)} tarjetas(s).")
    
    def hacer_compra(self, monto, indice_tarjeta= 0):
        """Realiza una compra en la tarjeta especificada (por el índice)"""
        if 0<= indice_tarjeta < len(TarjetCredito.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print("No existe la tarjeta con índice{indice_tarjeta}")
        return self
    def pagar_tarjeta(self, monto, indice_tarjeta= 0):
        """Realiza un pago en la tarjeta especificada (por el índice)"""
        if 0<= indice_tarjeta < len(TarjetCredito.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print(f"No existe la tarjeta con índice {indice_tarjeta}")
        return self