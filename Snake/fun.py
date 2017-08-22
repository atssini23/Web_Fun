#print 1 to 2000
def odd_even():
    for count in range (1,2000):
        if count % 2 == 0:
            print "Number is " + str(count) + ". This is an even number."
        else:
            print "Number is " + str(count) + ". This is an odd number."

# odd_even()

def multiply(arr,num):
    ret = []
    for x in arr:
        ret.append(x * num)
    return ret
a = [2,4,10,16]
b = multiply(a,5)
print b
