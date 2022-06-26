class Wallet: # Создание класса кошелек
    moneyOld = 1000  # Объявление переменных
    moneyNew = moneyOld # Переменная
    currency = "Рубль"
    person = "Иванов"
    def deposit(m): # Объявляем метод с переменной m, к которой мы будем обращаться
        Wallet.moneyNew = Wallet.moneyOld +m # В методе идет обращение к переменной класса Wallet - money. Потом мы записываем изменение данных кошелька
        print("Счет:", Wallet.person, "Валюта:", Wallet.currency, "Счет до изменения:", Wallet.moneyOld, "Счет после изменения:", Wallet.moneyNew,"Тип изменения: добавление")
        Wallet.moneyOld = Wallet.moneyNew # Записываем финальное изменение счета
    def withdraw(m):
        Wallet.moneyNew = Wallet.moneyOld -m # В методе идет обращение к переменной класса Wallet - money. Потом мы записываем изменение данных кошелька
        print("Счет:", Wallet.person, "Валюта:", Wallet.currency, "Счет до изменения:", Wallet.moneyOld, "Счет после изменения:", Wallet.moneyNew,"Тип изменения: списание")
        Wallet.moneyOld = Wallet.moneyNew # Записываем финальное изменение счета
Wallet.deposit(100) # Мы обращаемся к классу
Wallet.withdraw(200)