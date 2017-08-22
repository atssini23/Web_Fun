class Products(object):
    def __init__(self,price,item_name,weight,brand,cost,status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        print self.status
        return self

    def add_tax(self,tax):
        tax += tax * .10
        print tax
        return self

    def returns(self,reason):
        self.status = str("Defective")
        if (reason is "defective"):
            self.price = str("0")
        elif (reason is "like new"):
            self.staus  = "For Sale"
        elif (reason is "Used"):
            self.status = "used"
            self.price -= self.price * .20
        return self

    def displayInfo(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.cost
        print self.status
        return self


Product1 = Products(30,"Thing","1ld","Nike",20)
Product1.sell().add_tax(10).returns("Used").displayInfo()
