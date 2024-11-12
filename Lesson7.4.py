def common_elements():
    kratno_3 = {x for x in range(100) if x % 3 == 0}
    kratno_5 = {x for x in range(100) if x % 5 == 0}
    common_set = kratno_3 & kratno_5
    print(common_set)
    return common_set
common_elements()
