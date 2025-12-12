class Pagamento:
    def processar_pagamento(self, valor):
        raise NotImplementedError

class CartaoCredito(Pagamento):
    def __init__(self, numero_cartao, nome_titular, validade, cvv):
        self.numero_cartao = numero_cartao
        self.nome_titular = nome_titular
        self.validade = validade
        self.cvv = cvv
    
    def processar_pagamento(self, valor):
        return f"€{valor:.2f} com Cartão de Crédito ({self.numero_cartao})"
    
class Paypal(Pagamento):
    def __init__(self, email):
        self.email = email
    
    def processar_pagamento(self, valor):
        return f"€{valor:.2f} com PayPal (email: {self.email})"

class TransferenciaBancaria(Pagamento):
    def __init__(self, banco, agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
    
    def processar_pagamento(self, valor):
        return f"€{valor:.2f} com Transferência Bancária (banco: {self.banco}, conta: {self.conta})"
    
def realizar_pagamento(metodo_pagamento, valor):
    if not isinstance(metodo_pagamento, Pagamento):
        raise TypeError("O objeto deve ser uma instância de Pagamento")
    
    return metodo_pagamento.processar_pagamento(valor)

if __name__ == "__main__":
    cartao_credito = CartaoCredito(
        numero_cartao="1234 5678 9012 3456",
        nome_titular="João Silva",
        validade="12/25",
        cvv="123"
    )

    paypal = Paypal(email="joao.silva@email.com")

    transferencia = TransferenciaBancaria(
        banco="Banco Central",
        agencia="1234",
        conta="12345678"
    )

    resultados = [
        realizar_pagamento(cartao_credito, 150.00),
        realizar_pagamento(paypal, 200.00),
        realizar_pagamento(transferencia, 300.00)
    ]

    for resultado in resultados:
        print(resultado)