from collections import Counter
from solutions.bogof.bogof import bogof
from solutions.sum_of_checkout.sum import checkout_values
from solutions.valid_items.validate import check_if_values
from solutions.group_discount.discount import discount


def checkout(skus):

    list_of_items = list(skus)
    counter_of_items = Counter(list_of_items)

    dict_of_deals = {"A": {1 : 50, 3 : 130, 5: 200}, "B": {1 : 30, 2: 45}, "C": {1: 20},
        "D": {1: 15}, "E" : {1: 40}, "F" : {1: 10}, "G" : {1 : 20}, "H" : {1: 10, 5: 45, 10: 80},
        "I": {1: 35}, "J": {1: 60}, "K": {1: 70, 2: 120}, "L": {1: 90}, "M": {1: 15}, "N": {1: 40},
        "O": {1: 10}, "P": {1: 50, 5: 200}, "Q": {1: 30, 3: 80}, "R": {1: 50}, "S": {1: 20}, "T": {1: 20},
        "U": {1:40}, "V": {1: 50, 2:90, 3:130}, "W": {1: 20}, "X": {1: 17}, "Y": {1:20}, "Z": {1:21}}
    dict_of_bogof = {"E": {2: "B"}, "F" : {3 : "F"}, "N": {3: "M"}, "R": {3: "Q"}, "U": {4 : "U"}}


    if check_if_values(counter_of_items, dict_of_deals):
        counter_of_items = bogof(counter_of_items, dict_of_bogof, dict_of_deals)
        counter_of = discount(counter_of_items, dict_of_deals)

        return checkout_values(counter_of[1], dict_of_deals) + counter_of[0]
    else:
        return -1
