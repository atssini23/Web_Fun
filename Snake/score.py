import random
def grades():
    for i in range(1,10):
        grade = random.randint(60,100)
        if grade in range(90,100):
            print "Score: "+str(grade)+"; Your grade is A"
        if grade in range(80,90):
            print "Score: "+str(grade)+"; Your grade is B"
        if grade in range(70,80):
            print "Score: "+str(grade)+"; Your grade is C"
        if grade in range(60,70):
            print "Score: "+str(grade)+"; Your grade is D"
grades()
