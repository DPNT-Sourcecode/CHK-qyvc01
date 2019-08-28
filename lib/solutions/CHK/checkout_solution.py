from collections import Counter

def checkout(skus):
    checkoutValue = 0
    dictionaryOfCosts = {"A": 50, "B": 30, "C": 20, "D": 15}
    listOfItems = list(skus)
    cntOfItems = Counter(listOfItems)



