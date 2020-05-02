#Задание 4



class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name= name
        self.is_police = is_police

    def go(self):
        print("Автомобиль", self.name, "поехал")

    def stop(self):
        print("Автомобиль", self.name, "остановился")

    def left(self):
        print("Автомобиль", self.name, "повернул влево")

    def right(self):
        print("Автомобиль", self.name, "повернул вправо")

    def show_sheed(self):
        print('Автомобиль', self.name, 'едет со скоростью', self.speed)

    def police(self):
        if self.is_police:
            print('Автомобить', self.name, 'находится в использовании полицией')

        else:
            print(self.name, ' Гражданский автомобиль')

    def show_speed(self):
        print('Автомобиль', self.name, 'едет со скоростью', self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Автомобиль', self.name, 'едет со скоростью', self.speed)

        if self.speed > 40:
            print('Автомобиль едет со скоростью, превышающую допустимую на', self.speed - 40 , 'км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Автомобиль', self.name, 'едет со скоростью', self.speed)

        if self.speed > 60:
            print('Автомобиль едет со скоростью, превышающую допустимую на', self.speed - 60, 'км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)




kawasaki = SportCar(100, 'Red', 'Кавасаки', True)
mitsubisi = TownCar(65, 'White', 'Митсубиси', False)
belaz = WorkCar(30, 'Rose', 'Белаз', False)
police = PoliceCar(110, 'Blue',  'Жигули', True)

kawasaki.left()
kawasaki.right()
mitsubisi.go()
mitsubisi.stop()
belaz.police()
police.police()
kawasaki.police()
belaz.show_speed()
mitsubisi.show_speed()
