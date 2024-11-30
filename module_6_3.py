import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords=[0,0,0]
        self.speed=speed
    def move(self, dx, dy, dz):
        move_x=self._cords[0]+dx*self.speed
        move_y=self._cords[1]+dy*self.speed
        move_z=self._cords[2]+dz*self.speed
        if move_z<0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords=[move_x,move_y,move_z]
    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER >=5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

class Bird (Animal):
    beak = True #наличие клюва
    def lay_eggs(self):
        egs_mumber=random.randint(1,4)
        print(f'Here are(is) {egs_mumber} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        move_z=self._cords[2]-abs(dz)*.5*self.speed
        self._cords[2] = max(move_z, 0)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
     sound = "Click-click-click"
     def __init__(self, speed):
         super().__init__(speed)

     def speak(self):
         print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
