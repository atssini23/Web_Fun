
import random
x = .23945593
y = .798839238
def coins():
    recordList=[]
    head = 0
    tail = 0
    coins = random.randint(0,1)
    for i in range(1,2):
        coins = random.randint(0,1)
        if coins % 2 == 0:
            print "head"
        else:
            print "tail"
coins()

# "Attempt #"+(++)+":Throwing the coin...
# It's a"+str(coins)"...
# Got"+()+"head(s) so far
# and"+()+"tail(s) so far"
