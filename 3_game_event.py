class GameEventException(Exception):
    def __init__(self, event_type: str, details: dict):
        super().__init__(f"Ігрова подія: {event_type}")
        self.event_type = event_type
        self.details = details


# Приклад використання
def simulate_gameplay():
    """ Створюємо подію таку як смерть персонажа """
    raise GameEventException(
        event_type="Смерть",
        details={"Причина": "удар мечем", "вбивця": "Орк"}
    )


def simulate_level_up():
    """ Створюємо подію таку як підвищення рівня """
    raise GameEventException(
        event_type="Підвищення рівня",
        details={"Новий рівень": 5, "Бали досвіду": 1200}
    )


# Обробка подій
events = [simulate_level_up, simulate_gameplay]

for event_func in events:
    try:
        event_func()
    except GameEventException as ex:
        if ex.event_type == "Смерть":
            print(f"Персонаж загинув. Причина: {ex.details['Причина']}. Вбивця: {ex.details.get('вбивця')}")
        elif ex.event_type == "Підвищення рівня":
            print(
                f"Рівень прокачано! Новий рівень: {ex.details['Новий рівень']}, Бали досвіду: {ex.details['Бали досвіду']}")
        else:
            print(f"Інша подія: {ex.event_type}, деталі: {ex.details}")
