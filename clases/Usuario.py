class User:

    MAXIMO = 3

    def __init__(self, username,lastName, email_address):
        self.name = username
        self.lastName = lastName
        self.email = email_address
        self.accounts = []

    def agregar_cuenta(self, bankAccount):
        if len(self.accounts) < self.MAXIMO:
            self.accounts.append(bankAccount)
        else:
            print(f"Superaste el maximo de {self.MAXIMO} cuentas.")
            return self

    def deposito(self, indice, amount=0):
        self.accounts[indice].account_balance += amount

    def retiro(self, amount=0):
        self.account_balance -= amount

    def balance(self):
        print(f"El Balance de {self.name} {self.lastName} es {self.account_balance} Dolares")

if __name__ == "__main__":
    pablo = User("Pablo","Sepulveda", "p.sepulvedamorande@gmail.com")
    magdalena = User("Magdalena","Rolando", "magdalena@gmail.com")
    juan = User ("Juan","Juani", "juan@gmail.com")

    print(pablo.account_balance)
    print(magdalena.account_balance)

    pablo.deposito(100)
    magdalena.deposito(1000)
    juan.deposito(100)
    pablo.deposito(100)
    pablo.retiro(80)
    pablo.deposito(100)
    juan.deposito(100)
    juan.deposito(100)
    pablo.deposito(100)
    magdalena.retiro(500)
    pablo.retiro(25)
    juan.retiro(57)
    pablo.balance()
    magdalena.balance()
    juan.balance()