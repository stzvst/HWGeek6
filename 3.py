#Задание 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__( name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(full_name)
        return full_name

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        print(total_income)
        return total_income


person = Position('Иван', "Романович", 'Консультант', 20000, 1000)

person.get_full_name()

person.get_total_income()

print(person.position)

print(person._income)