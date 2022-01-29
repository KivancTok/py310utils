def search(search_list: list, value):
    for i in range(len(search_list)):
        if search_list[i] == value:
            print(f"Item found! Index: {i}")
            break

    else:
        print("Not found.")
