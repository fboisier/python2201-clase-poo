from clases import BankAccount
from clases import User

pancho = User('Pancho','Boisier', 'jajaja@jaja.com')

cuenta1 = BankAccount()
cuenta2 = BankAccount()

pancho.agregar_cuenta(cuenta1)
pancho.agregar_cuenta(cuenta2)
pancho.agregar_cuenta(BankAccount())
pancho.agregar_cuenta(cuenta2)
pancho.agregar_cuenta(BankAccount())

pancho.deposito(2,100)

for cuenta in pancho.accounts:
    print("BALANCE :", cuenta.account_balance)


print(User.MAXIMO)