# checks if items are valid against dictionary
def check_if_values(counter_of_items, dict_of_deals):
    for item in counter_of_items:
        if item not in dict_of_deals:
            return 0
            break
    return 1
