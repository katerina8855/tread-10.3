import threading
import time

lock = threading.Lock()
def account_number():
    import random
    account = ''
    for i in range(5):
        account += random.choice(list('0123456789'))
    return account


account = account_number()
balance = int(input('Ваш взнос на счет: '))
print(f'{"":*^50}')
print(f'Баланс счета №"{account}  {balance}')
print(f'{"":*^50}')


class BankAccount(threading.Thread):
    def __init__(self, amount_incoming, amount_spending):
        super().__init__()
        self.amount_incoming = amount_incoming
        self.amount_spending = amount_spending
        global account, balance
        self.balance = balance

    def incoming_money(self):
        with lock:
            for i in range(5):
                time.sleep(1)
                global balance
                balance += self.amount_incoming
                print(f'Сумма пополнения = {self.amount_incoming},  баланс счета №{account} = {self.balance}')
                self.balance = balance
            return self.balance

    def spending_money(self):
        with lock:
            for j in range(5):
                time.sleep(1)
                global balance
                balance += -self.amount_spending
                print(f'Сумма списания = {-self.amount_spending}, баланс счета №{account} = {self.balance}')
                self.balance = balance
            return self.balance

    def run(self):
        a = self.amount_incoming * 5
        b = self.amount_spending * 5
        if a > 0 and b == 0:
            BankAccount.incoming_money(self)
            print(f'{a} баланс счета №{account} = {balance}\n')
        elif b > 0 and a == 0:
            BankAccount.spending_money(self)
            print(f'{-b}, баланс счета №{account} = {balance}')
        elif a == 0 and b == 0:
            print(f'Баланс счета №{account} остался без изменений'.upper())
        else:
            print('Один из аргументов класса'.upper() + ' BankAccount() ' + 'должен быть равен 0'.upper())


incoming = BankAccount(10, 0)
spending = BankAccount(0, 5)
incoming.start()
spending.start()
incoming.join()
spending.join()
# time.sleep(11)
print(f'\n{"":*^70}')
print(f'Баланс счета №{account} = {balance}')
print(f'{"":*^70}')