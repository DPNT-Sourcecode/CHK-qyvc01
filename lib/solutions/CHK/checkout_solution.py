from collections import Counter

def checkout(skus):
    checkoutValue = 0
    dictionaryOfCosts = {"A": 50, "B": 30, "C": 20, "D": 15}
    dictionaryOfDeals = {"A": 130, "B": 45}
    listOfItems = list(skus)
    cntOfItems = Counter(listOfItems)

    for item in cntOfItems:
        
        checkoutValue += dictionaryOfCosts[item] * cntOfItems[item]

    return checkoutValue




