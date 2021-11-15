def bool_filter(change_list, bool_list):
    chlist = [i for index, i in enumerate(change_list) if bool_list[index]]
    return chlist
