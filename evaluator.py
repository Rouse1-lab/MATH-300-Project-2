#We define our continued fraction function
def c_f(c0, k, l, M):
    #c0 is where we begin
    #k this is the value of the upperside of the fraction
    #l this the value of the lower side of the fraction
    #M is how many terms we want to use

    #We set the conditionto see if M is positive or not
    if M < 1:
        print("M is positive")
        return None
    #We begin calculating from the last denominator of the fraction, and the float is used to give it in decimal value.
    number = float(l(M))
    #We form a loop that counts backward from M -1 to 1
    for m in range(M - 1, 0, -1):
        if number == 0:
            print("We divide by 0")
            return None
        #This equation is to find the value of the continued fraction by finding all the values of denominators and numerators in an upward direction starting from the very bottom
        number = float(l(m)) + float(k(m + 1)) / number
        #This a loop to check if it is null prior to dividing by its value, and it stops when it is null
        if number == 0:
            print("Err: We divide by 0")
            return None
    #This will combine the initial value c0 with the initial numerator over the number given by the loop.
    return float(c0) + float(k(1)) / number