def bogof(counter_of_items, dict_of_bogof, dict_of_deals):
    for item in counter_of_items:

        if item in dict_of_bogof:

            for x in dict_of_bogof[item]:

                if dict_of_bogof[item][x] in counter_of_items:
                    how_many_bogofs = counter_of_items[item] // x

                    counter_of_items[dict_of_bogof[item][x]] = counter_of_items[dict_of_bogof[item][x]] - how_many_bogofs

    counter_of_items = +counter_of_items

    return counter_of_items

