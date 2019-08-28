from collections import Counter

def checkout(skus):
    checkoutValue = 0
    dictionaryOfCosts = {"A": 50, "B": 30, "C": 20, "D": 15}
    dictionaryOfDealsCosts = {"A": 130, "B": 45}
    dictionaryOfDeals = {"A": 3, "B": 2}

    listOfItems = list(skus)
    cntOfItems = Counter(listOfItems)

    for item in cntOfItems:
        if (item in dictionaryOfDeals) and (cntOfItems[item] % dictionaryOfDeals[item] == 0):
            checkoutValue += dictionaryOfDealsCosts[item] * (cntOfItems[item] / dictionaryOfDeals[item])
        else:
            checkoutValue += dictionaryOfCosts[item] * cntOfItems[item]

    return checkoutValue






