def checkout_values(counter_of_items, dict_of_deals):


    # loops through trying to find best deal on items
    # does this by subtracting max until it can do no more, pops the max and
    # loops with second max and so on...
    value = 0
    for item in counter_of_items:
        if item in dict_of_deals:
            n = counter_of_items[item]
            a = list(dict_of_deals[item])
            ans = []
            while n > 0:
                n -= max(a)
                if n == 0:
                    ans.append(max(a))
                    break
                if n > 0:
                    ans.append(max(a))
                if n < 0:
                    n += max(a)
                    a.pop(a.index(max(a)))
        for x in ans:
            value += dict_of_deals[item][x]

    return value


