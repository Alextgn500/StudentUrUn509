import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.deposit_count = 0
        self.take_count = 0

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            self.deposit_count += 1
            print(f"Пополнение #{self.deposit_count}: {amount}. Баланс: {self.balance}\n")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        while self.take_count < 100:
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}\n")
            if amount <= self.balance:
                self.balance -= amount
                self.take_count += 1
                print(f"Снятие #{self.take_count}: {amount}. Баланс: {self.balance}\n")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
                # Добавляем небольшую задержку, чтобы дать шанс другому потоку выполниться
                time.sleep(0.001)


# Создаем объект класса Bank
bk = Bank()

# Создаем и запускаем потоки
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс и количество операций
print(f'\nИтоговый баланс: {bk.balance}')
print(f'Всего операций пополнения: {bk.deposit_count}')
print(f'Всего операций фактического снятия: {bk.take_count}')
