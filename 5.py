#Задание 5





class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отприсовки")
        return


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, '. Отрисовано ручкой')
        return


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, '. Отрисовано карандашем')
        return


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, '. Отрисовано маркером')
        return


pen = Pen('Тута тыкать ручкой')
pencil = Pencil('Отрисовать все карандашиком')
handle = Handle('Зачеркни маркером')

pen.draw()
pencil.draw()
handle.draw()