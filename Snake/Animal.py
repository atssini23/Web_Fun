class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def displayhealth(self):
        print "Health:"+str(self.health)
        return self

    def walk(self):
        print "Walk"
        self.health -= 1
        return self

    def run(self):
        print "Run"
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Animal, self).__init__()
        self.health = 150

    def pet(self):
        print "Pet"
        self.health += 5
        return self

class Dragon(Animal):
        def __init__(self,name):
            super(Animal, self).__init__()
            self.health = 170

        def fly(self):
            print "Fly"
            self.health -= 10
            return self

        def displayhealth(self):
            print "I am a Dragon"
            return self

Animal1 = Animal("Stacy", 100)
Animal1.walk().walk().walk().run().run().displayhealth()

Dog1 = Dog("Bud")
Dog1.walk().walk().walk().run().run().pet().displayhealth()

Dragon1 = Dragon("uy")
Dragon1.walk().walk().walk().run().run().fly().displayhealth()
