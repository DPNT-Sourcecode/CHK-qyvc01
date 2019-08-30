from collections import Counter
from solutions.bogof.bogof import bogof
from solutions.sum_of_checkout.sum import checkout_values
from solutions.valid_items.validate import check_if_values


def checkout(skus):

    list_of_items = list(skus)
    counter_of_items = Counter(list_of_items)

    dict_of_deals = {"A": {1 : 50, 3 : 130, 5: 200}, "B": {1 : 30, 2: 45}, "C": {1: 20}, "D": {1: 15}, "E" : {1: 40}}
    dict_of_bogof = {"E": {2: "B"}}


    if check_if_values(counter_of_items, dict_of_deals):
        counter_of_items = bogof(counter_of_items, dict_of_bogof, dict_of_deals)

        return checkout_values(counter_of_items, dict_of_deals)
    else:
        return -1
