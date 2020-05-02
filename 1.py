#Задание 1
from time import sleep

def in_sleep(time_out):
    t = 0
    while t < time_out:
        t +=1
        print(t)
        sleep(1)

class Svetofor:
    __color = ['RED', 'YELLOW', 'GREEN']

    def running(self, times):
        j = 0
        while j < times:
           i = 0
           while i < 3:
               print ('Светофор горит ->', Svetofor.__color[i])
               if i == 0:
                   in_sleep(7)
               elif i == 1 :
                   in_sleep(5)
               elif i == 2:
                   in_sleep(3)

               i += 1
           j += 1



Svetofor = Svetofor()
Svetofor.running(1)