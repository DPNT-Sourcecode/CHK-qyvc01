def checkout_values(counter_of_items, dict_of_deals):


    # loops through trying to find best deal on items
    # does this by subtracting max until it can do no more, pops the max and
    # loops with second max and so on...
    value = 0
    for item in counter_of_items:
        if item in dict_of_deals:
            num = counter_of_items[item]
            list_of_dict = list(dict_of_deals[item])
            result = []
            while num > 0:
                num -= max(list_of_dict)
                if num == 0:
                    result.append(max(list_of_dict))
                    break
                if num > 0:
                    result.append(max(list_of_dict))
                if num < 0:
                    num += max(list_of_dict)
                    list_of_dict.pop(list_of_dict.index(max(list_of_dict)))
        for x in result:
            value += dict_of_deals[item][x]

    return value
