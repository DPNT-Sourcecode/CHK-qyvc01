import itertools

def discount(counter_of_items, dict_of_deals):

  value_of_discount = 0

  list_of_group = {"S": 15, "T": 15, "X": 15, "Y": 15, "Z": 15}

  # create mini counter group
  groups = {}
  for item in counter_of_items:
    if item in list_of_group:
      groups[item] = counter_of_items[item]

  while sum(groups.values()) & len(groups) >= 3:

    # find all possible combinations
    combin_found_groups = list(itertools.combinations(groups, 3))
    # associate values to possible combinations
    list_of_tuple_prices = []
    for item in combin_found_groups:
      list_of_prices = []
      for value in item:
        list_of_prices.append(dict_of_deals[value][1])
      list_of_tuple_prices.append(list_of_prices)

    # find index of max combination
    compre = [sum(x) for x in list_of_tuple_prices]
    index_of_max = compre.index(max(compre))

    for item in combin_found_groups[index_of_max]:
      groups[item] = groups[item] - 1
      value_of_discount += list_of_group[item]



  for item in groups:
    counter_of_items[item] = groups[item]


  counter_of_items = +counter_of_items

  return [value_of_discount, counter_of_items]
