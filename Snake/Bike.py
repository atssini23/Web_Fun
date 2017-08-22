class Bike(object):
    """A class that makes various types of Bikes"""
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price:"+str(self.price)
        print "Max Speed:"+str(self.max_speed)+"mph"
        print "Total Miles:"+str(self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self



bike1 = Bike(200,"25")
bike2 = Bike(500, "7")
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
