from collections import Counter
from bogof.bogof import bogof
from sum_of_checkout.sum import checkout_values
from valid_items.validate import check_if_values




def checkout(skus):

    list_of_items = list(skus)
    counter_of_items = Counter(list_of_items)
    
    dict_of_deals = {"A": {1 : 50, 3 : 130, 5: 200}, "B": {1 : 30, 2: 45}, "C": {1: 20}, "D": {1: 15}, "E" : {1: 40}}
    dict_of_bogof = {"E": {2: "B"}}



    for item in cnt_of_items:
        if item in dictionary_of_deals:
            if item in dictionary_of_special_offers and cnt_of_items[item] % dictionary_of_deals[item] == 0:
                divisible = cnt_of_items[item] // dictionary_of_deals[item] # no remainder
                checkout_value += dictionary_of_costs[item] * cnt_of_items[item]
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

def bogof(letter):
    dictionary_of_bogof = {"E" : "B"}
    dictionary_of_costs

