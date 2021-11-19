def bool_filter(change_list, bool_list):
    chlist = [i for index, i in enumerate(change_list) if bool_list[index]]
    return chlist


def bool_not_filter(change_list, bool_list):
    chlist = [i for index, i in enumerate(change_list) if not bool_list[index]]
    return chlist
