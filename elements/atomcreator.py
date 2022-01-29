def create_atom():
    name = input("Atom name: ")
    abbr = input("Atom abbreviation: ")
    atomic_num = int(input("Atomic number: "))
    atomic_mass = 0
    amt_types = int(input("Amount of types: "))
    per_remain = 100.0
    types = []
    type_chance = []

    for i in range(amt_types):
        types.append(int(input(f"Type {i + 1} (as an integer): ")))
        print(f"Percentage remaining: {per_remain}")
        type_chance.append((ch_occ := float(input("Chance of occurrence: "))))
        per_remain -= ch_occ
        per_remain = round(per_remain, 1)

    for i in range(amt_types):
        atomic_mass += round(types[i] * (type_chance[i] / 100), 2)

    print((f"""Name: {name} ({abbr})
Atomic Number: {atomic_num}
Atomic Mass: {round(atomic_mass, 2)}
Types: {str(types).removeprefix("[").removesuffix("]")}
Chance of occurence: {str(type_chance).removeprefix("[").removesuffix("]")}"""))

    with open(f"{name}.json", "w") as f:
        f.write(f"""\x7b
    "name": "{name}",
    "abbr": "{abbr}",
    "atomic_num": {atomic_num},
    "atomic_mass": {atomic_mass},
    "types": {types},
    "type_chance": {type_chance}
\x7d""")
