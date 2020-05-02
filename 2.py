#Задание 2


class Road:
    def __init__(self, _lenght, _width):
        self._lengh = _lenght
        self._width = _width


    def Mass(self):
        mass = 25
        glubina = 5
        massa = self._width * self._lengh * mass * glubina
        return massa / 1000



class Build_road(Road):
    def __init__(self, _lenght, _width):
        super().__init__(_lenght, _width)


raschet = Build_road(20,5000)
print (raschet.Mass(), "тонн")