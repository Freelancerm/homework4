class InsufficientResourcesException(Exception):
    def __init__(self, required_resource: str, required_amount: int, current_amount: int):
        super().__init__(f"Не вистачає наступного ресурсу: {required_resource}")
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount


# Приклад використання дії у грі
def cast_spell(current_mana: int, mana_cost: int):
    """ Спроба використати заклинання """
    if current_mana < mana_cost:
        raise InsufficientResourcesException(
            required_resource="мана",
            required_amount=mana_cost,
            current_amount=current_mana
        )
    new_mana = current_mana - mana_cost
    print("Заклинання успішно використане!")
    print(f"Залишок ресурсу 'мана': {new_mana}")
    return new_mana


# Використання
print(f"Приклад використання заклинання при умові що не вистачає ресурсу:")
try:
    mana = 10
    mana_required = 25
    mana = cast_spell(mana, mana_required)
except InsufficientResourcesException as ex:
    print(
        f"Недостатньо ресурсу '{ex.required_resource}'.\n"
        f"Потрібно: {ex.required_amount}, доступно: {ex.current_amount}\n"
    )

print(f"Приклад використання заклинання при умові що ресурсу вистачає:")
try:
    mana = 222
    mana_required = 25
    mana = cast_spell(mana, mana_required)
except InsufficientResourcesException as ex:
    print(
        f"Недостатньо ресурсу '{ex.required_resource}'.\n"
        f"Потрібно: {ex.required_amount}, доступно: {ex.current_amount}"
    )
