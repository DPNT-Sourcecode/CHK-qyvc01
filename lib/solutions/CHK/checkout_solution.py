from collections import Counter

def checkout(skus):

    checkout_value = 0
    dictionary_of_costs = {"A": 50, "B": 30, "C": 20, "D": 15}
    dictionary_of_deals_costs = {"A": 130, "B": 45}
    dictionary_of_deals = {"A": 3, "B": 2}

    list_of_items = list(skus)
    cnt_of_items = Counter(list_of_items)

    for item in cnt_of_items:
        if (item in dictionary_of_deals) and (cnt_of_items[item] % dictionary_of_deals[item] == 0):
            checkout_value += dictionary_of_deals_costs[item] * (cnt_of_items[item] / dictionary_of_deals[item])
        elif item not in dictionary_of_costs:
          checkout_value = -1
          break
        else:
            checkout_value += dictionary_of_costs[item] * cnt_of_items[item]

    return int(checkout_value)



