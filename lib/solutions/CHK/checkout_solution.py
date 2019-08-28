from collections import Counter

def checkout(skus):

    checkout_value = 0
    dictionary_of_costs = {"A": 50, "B": 30, "C": 20, "D": 15, "E" : 40}
    dictionary_of_deals_costs = {"A": 130, "B": 45}
    dictionary_of_deals = {"A": [3,5], "B": 2, "E" : 2}
    dictionary_of_special_offers = {"E": "B"}
    list_of_items = list(skus)
    cnt_of_items = Counter(list_of_items)

    for item in cnt_of_items:
        if item in dictionary_of_deals:
            if item in dictionary_of_special_offers and cnt_of_items[item] % dictionary_of_deals[item] == 0:
                divisible = cnt_of_items[item] // dictionary_of_deals[item] # no remainder
                checkout_value -= divisible * dictionary_of_costs[dictionary_of_special_offers[item]]
            else:
                diff = cnt_of_items[item] % dictionary_of_deals[item] # the diff using modulo
                divisible = cnt_of_items[item] // dictionary_of_deals[item] # no remainder
                checkout_value += (dictionary_of_costs[item] * diff) + (dictionary_of_deals_costs[item] * divisible)
        elif item not in dictionary_of_costs:
            return -1
        else:
            checkout_value += dictionary_of_costs[item] * cnt_of_items[item]

    return int(checkout_value)




