import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.activity = 1
        self.alive = True

    def to_eat(self):
        print("Time to eating")
        self.hunger += 1.1
        self.activity -= 0.1

    def to_play(self):
        print("Time to game")
        self.hunger -= 1
        self.activity += 0.1


    def is_alive(self):
        if self.hunger <= 15:
            print("Very want to eat")
            self.alive = False

        elif self.activity <= 0:
            print("Very sad cat")
            self.alive = False

        elif self.hunger >= 50:
            print("Very fat cat")
            self.alive = False


    def end_of_day(self):
        print(f"hunger = {self.hunger}")
        print(f"activity = {self.activity}")

    def live(self, day):
        day = "day" + str(day) + "of" + self.name + "life"
        print(day)

        live_cube = random.randint(1, 2)

        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_play()



        self.end_of_day()
        self.is_alive()


Barsik = Cat(name="Barsik")

for day in range(365):
    if Barsik.alive == False:
        break


    Barsik.live(day)



