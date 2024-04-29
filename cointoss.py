import random
def cointoss():
    toss=random.randint(0,1)
    if toss==0:
        return "Heads"
    else:
        return "Tails"
result=cointoss()
print("the result of coin toss is : ",result)
