class InsufficientFundsException(Exception):
    def __init__(self, required_amount: float, current_balance: float, currency: str = "UAH",
                 transaction_type: str = "operation"):
        super().__init__("Не вистачає коштів на рахунку")
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type


# Приклад дії (придбання товару)
def purchase(current_balance: float, price: float, currency: str = "UAH"):
    """ Спроба зняти кошти з рахунку за покупку """
    if balance < price:
        raise InsufficientFundsException(
            required_amount=price,
            current_balance=current_balance,
            currency=currency,
            transaction_type="purchase"
        )
    new_balance = balance - amount
    print(f"Покупка успішна! Сума:{amount:.2f} {currency}.")
    print(f"Залишок на рахунку: {new_balance:.2f} {currency}.")
    return new_balance


# Використання:
print(f"Спроба здійснити покупку при умові що бракує коштів")
try:
    balance = 1000
    amount = 1500
    balance = purchase(balance, amount, currency="UAH")
except InsufficientFundsException as ex:
    print(f"Недостатньо коштів для операції '{ex.transaction_type}'.")
    print(f"Потрібно: {ex.required_amount:.2f} {ex.currency},")
    print(f"Доступно на балансі: {ex.current_balance:.2f} {ex.currency}.\n")

print("Спроба здійснити покупку при умові що коштів вистачає")
try:
    balance = 2000
    amount = 1499.99
    balance = purchase(balance, amount, currency="UAH")
except InsufficientFundsException as ex:
    print(f"Недостатньо коштів для операції '{ex.transaction_type}'.")
    print(f"Потрібно: {ex.required_amount:.2f} {ex.currency},")
    print(f"Доступно на балансі: {ex.current_balance:.2f} {ex.currency}.")
