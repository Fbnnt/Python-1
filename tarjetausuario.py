#Fabian Vargas

class TarjetCredito:
    tarjetas = []
    def __init__(self, saldo_pagar=0, limite_credito=10000,interes=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.interes = interes
        TarjetCredito.tarjetas.append(self)

    def comprar(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print(f"Compra realizada: ${monto:,}. Nuevo saldo: ${self.saldo_pagar:,}")
        else:
            print("Tarjeta rechazada. haz alcanzado tu limite de crédito.")
        return self

    def pago(self, monto):       
        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            if self.saldo_pagar < 0:
                self.saldo_pagar = 0
            print(f"Pago realizado: ${monto:,}. Nuevo saldo: ${self.saldo_pagar:,}")
        else:
            print("El monto a pagar excede el saldo pendiente.")
        return self
    
    def mostrar_info_tarjeta(self):
        print("-----------------Información de la tarjeta-------------------")
        print(f"Saldo a pagar: ${self.saldo_pagar:,}")
        print(f"Límite de crédito: ${self.limite_credito:,}")
        print("-------------------------------------------------------------")
        return self
    
    def cobrar_interes(self, interes=0.02):
        self.saldo_pagar += self.saldo_pagar * self.interes
        print(f"Interés cobrado, Nuevo saldo: ${self.saldo_pagar:,.2f}")
        return self
    

    @classmethod
    def mostra_todas_tarjetas(cls):
        for i, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"Tarjeta {i}:Saldo:${tarjeta.saldo_pagar:,}, Límite: ${tarjeta.limite_credito:,}, Interés: {tarjeta.interes:.2%}")

print("==== Tarjeta 1===")
tarjeta1 = TarjetCredito()
tarjeta1.comprar(50000).comprar(2000).pago(10000).cobrar_interes(0.02).mostrar_info_tarjeta()

print("=========================================================")

print("==== Tarjeta 2===")
tarjeta2 = TarjetCredito(limite_credito= 80000, interes=0.03)
tarjeta2.comprar(70000).comprar(5000).pago(40000).cobrar_interes().mostrar_info_tarjeta()

print("=========================================================")

print("==== Tarjeta 3===")
tarjeta3 = TarjetCredito(limite_credito= 120000, interes=0.01)
tarjeta3.comprar(50000).comprar(2000).pago(10000).cobrar_interes().mostrar_info_tarjeta()

print("=========================================================")