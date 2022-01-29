def replace_from_list(__old_c: list[str], __new_c: list[str], __base: str) -> str:
    for i in range(len(__new_c)):
        __base = __base.replace(__old_c[i], __new_c[i])
    return __base
