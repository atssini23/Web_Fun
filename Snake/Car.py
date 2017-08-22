class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print "Price:",self.price
        print "Speed:",str(self.speed)
        print "Fuel:",str(self.fuel)
        print "Mileage:",str(self.mileage)
        if (self.price >= 10000):
            print  ("Tax: 0.15")
        else:
            print ("Tax: 0.12")
        return self

Car1 = Car(2000,"35mph","Full","15mpg")
Car1.display_all()
Car2 = Car(1300,"50mph","Not Full","19mpg")
Car2.display_all()
Car3 = Car(5000,"70mph","Full","28mpg")
Car3.display_all()
Car4 = Car(1800,"35mph","Full","25mpg")
Car4.display_all()
Car5 = Car(60000,"120mph","Full","19mpg")
Car5.display_all()
Car6 = Car(58000,"200mph","Not Full","37mpg")
Car6.display_all()
