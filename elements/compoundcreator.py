import json


def create_compound():
    atom_infos = []
    atom_names = []
    atomic_masses = []
    atomic_mass_total = 0

    comp_name = input("Compound name: ")
    amt_atoms = int(input("Amount of atoms: "))

    for i in range(amt_atoms):
        with open(f"{input('Get atom data from: ')}.json", "r", encoding="utf-8") as f:
            atom_infos.append(json.load(f))

        atom_infos[i]["amt_in_comp"] = int(input("Amount of the atom: "))
        if atom_infos[i]["amt_in_comp"] == 1:
            pass

        else:
            atom_infos[i]["name"] += f" ({atom_infos[i]['amt_in_comp']})"
            atom_infos[i]["atomic_num"] *= atom_infos[i]["amt_in_comp"]
            atom_infos[i]["atomic_mass"] *= atom_infos[i]["amt_in_comp"]

        atom_names.append(atom_infos[i]["name"])
        atomic_masses.append(atom_infos[i]["atomic_mass"])
        atomic_mass_total += atomic_masses[i]

    print(f"""Name: {comp_name}
Atoms: {str(atom_names).replace("[", "").replace("]", "").replace("'", "")}
Atomic Mass: {atomic_mass_total}""")

    with open(f"{comp_name}.json", "w") as f:
        f.write(json.dumps(f"""\x7b
    "comp_name": "{comp_name}",
    "atoms": "{atom_names}",
    "atomic_mass": "{round(atomic_mass_total, 2)}"
\x7d"""))
