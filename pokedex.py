import json
import sys
import textwrap
import argparse
from urllib.request import urlopen
from PIL import Image
import datetime
import platform
import getpass


def json_init():
    with open('pokemon.json') as json_pokemon:
        data_dict = json.load(json_pokemon)
        return data_dict


def list_option():
    dictionary = json_init()
    print("** LIST OF POKEMON **")
    for pokemon in dictionary:
        print(pokemon['pkdx_id'], pokemon['name'])
    print("")


def next_evo(dictionary, pokemon_name):
    for pokemon in dictionary:
        if pokemon['name'] == pokemon_name:
            for key in pokemon.keys():
                if key == 'evolutions':
                    try:
                        if len(pokemon['evolutions']) == 1:
                            pokemons_next_evo = pokemon['evolutions'][0]['to']
                            if pokemon['evolutions'][0]['method'] == 'level_up':
                                print("Evolves by", pokemon['evolutions'][0]['method'].replace("_", " "), "at",
                                      pokemon['evolutions'][0]['level'], "to", pokemon['evolutions'][0]['to'])
                            else:
                                print("Evolves by", pokemon['evolutions'][0]['method'].replace("_", " "), "to",
                                      pokemon['evolutions'][0]['to'])
                            next_evo(dictionary, pokemons_next_evo)

                        elif len(pokemon['evolutions']) > 1:
                            print(pokemon_name, "can evolve to", len(pokemon['evolutions']), "different pokemon:")
                            i = 0
                            while i < len(pokemon['evolutions']):
                                print("Evolves by", pokemon['evolutions'][i]['method'].replace("_", " "), "to",
                                      pokemon['evolutions'][i]['to'])
                                i += 1
                    except IndexError:
                        continue


def info_option(pokemon_name):
    dictionary = json_init()
    found = False

    for pokemon in dictionary:
        if pokemon['name'] == pokemon_name:
            found = True
            print("id: ", pokemon['pkdx_id'])
            print("name: ", pokemon['name'])
            print("description: ", "\n".join(textwrap.wrap(pokemon['description'], 180)))
            if len(pokemon['types']) == 1:
                print("type: ", pokemon['types'][0])
            elif len(pokemon['types']) == 2:
                print("types: ", pokemon['types'][0], "/", pokemon['types'][1])
            for key in pokemon.keys():
                if key == 'evolutions':
                    next_evo(dictionary, pokemon_name)
    if not found:
        print("Error: unknown pokemon")
    print("")


def get_weakness(type_name):
    if type_name == "bug":
        return ['fire', 'flying', 'rock']
    elif type_name == "dragon":
        return ['ice', 'dragon', 'fairy']
    elif type_name == "electric":
        return ['ground']
    elif type_name == "fairy":
        return ['poison', 'steel']
    elif type_name == "fighting":
        return ['flying', 'psychic', 'fairy']
    elif type_name == "fire":
        return ['water', 'ground', 'rock']
    elif type_name == "flying":
        return ['electric', 'ice', 'rock']
    elif type_name == "ghost":
        return ["ghost"]
    elif type_name == "grass":
        return ['fire', 'ice', 'poison', 'flying', 'bug']
    elif type_name == "ground":
        return ['water', 'grass', 'ice']
    elif type_name == "ice":
        return ['fire', 'fighting', 'rock', 'steel']
    elif type_name == "normal":
        return ["fighting"]
    elif type_name == "poison":
        return ['ground', 'psychic']
    elif type_name == "psychic":
        return ['bug', 'ghost']
    elif type_name == "rock":
        return ['water', 'grass', 'fighting', 'ground', 'steel']
    elif type_name == "steel":
        return ['fire', 'fighting', 'ground']
    elif type_name == "water":
        return ['grass', 'electric']


def get_resistance(type_name):
    if type_name == "bug":
        return ['grass', 'fighting', 'ground']
    elif type_name == "dragon":
        return ['fire', 'water', 'grass', 'electric']
    elif type_name == "electric":
        return ['electric', 'flying']
    elif type_name == "fairy":
        return ['fighting', 'bug']
    elif type_name == "fighting":
        return ['bug', 'rock']
    elif type_name == "fire":
        return ['fire', 'grass', 'ice', 'bug', 'steel', 'fairy']
    elif type_name == "flying":
        return ['grass', 'fighting', 'bug']
    elif type_name == "ghost":
        return ["poison", 'bug']
    elif type_name == "grass":
        return ['water', 'grass', 'electric', 'ground']
    elif type_name == "ground":
        return ['poison', 'rock']
    elif type_name == "ice":
        return ['ice']
    elif type_name == "normal":
        return []
    elif type_name == "poison":
        return ['grass', 'fighting', 'poison', 'bug', 'fairy']
    elif type_name == "psychic":
        return ['fighting', 'psychic']
    elif type_name == "rock":
        return ['normal', 'fire', 'poison', 'flying']
    elif type_name == "steel":
        return ['normal', 'grass', 'ice', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'steel', 'fairy', ]
    elif type_name == "water":
        return ['fire', 'water' 'ice', 'steel']


def weakness_option(pokemon_name):
    dictionary = json_init()
    found = False
    list_to_convert = []
    scd_list_to_convert = []

    for pokemon in dictionary:
        if pokemon['name'] == pokemon_name:
            result = "is weak to:"
            found = True
            if len(pokemon['types']) == 1:
                list_to_convert = get_weakness(pokemon['types'][0])
                for element in list_to_convert:
                    result = result + " " + element
            elif len(pokemon['types']) == 2:
                list_to_convert = get_weakness(pokemon['types'][0])
                scd_list_to_convert = get_weakness(pokemon['types'][1])
                list_wo_duplicate = list(set(list_to_convert + scd_list_to_convert))
                for element in list_wo_duplicate:
                    result = result + " " + element
            print(pokemon['name'], result)
    if not found:
        print("Error: unknown pokemon")
    print("")


def resistance_option(pokemon_name):
    dictionary = json_init()
    found = False
    list_to_convert = []
    scd_list_to_convert = []

    for pokemon in dictionary:
        if pokemon['name'] == pokemon_name:
            result = "is resisting:"
            found = True
            if len(pokemon['types']) == 1:
                list_to_convert = get_resistance(pokemon['types'][0])
                for element in list_to_convert:
                    result = result + " " + element
            elif len(pokemon['types']) == 2:
                list_to_convert = get_resistance(pokemon['types'][0])
                scd_list_to_convert = get_resistance(pokemon['types'][1])
                list_wo_duplicate = list(set(list_to_convert + scd_list_to_convert))
                for element in list_wo_duplicate:
                    result = result + " " + element
            print(pokemon['name'], result)
    if not found:
        print("Error: unknown pokemon")
    print("")


def picture_option(pokemon_name):
    dictionary = json_init()
    found = False

    for pokemon in dictionary:
        if pokemon['name'] == pokemon_name:
            found = True
            img = Image.open(urlopen(pokemon['image_url']))
            img.show()
    if not found:
        print("Error: unknown pokemon")
    print("")


def team_option(team):
    dictionary = json_init()
    user_name = getpass.getuser()
    current_date = str(datetime.date.today())
    i = 1
    found = False
    while i < 7:
        found = False
        for pokemon in dictionary:
            if pokemon['name'] == team[i].title():
                found = True
        if not found:
            print(team[i].title(),
                  "can't be added to your team cause he doesn't exist.\n Please check on the list (with -l , "
                  "--list) the pokemon that can be added to the team.")
            break
        i += 1
    i = 1
    if found:
        f = open(team[0] + ".txt", "a")
        f.write(str("Team created by " + user_name + " on " + current_date + ":") + "\n__________________\n")
        while i < 7:
            for pokemon in dictionary:
                if pokemon['name'] == team[i].title():
                    id_pkm = str(pokemon['pkdx_id'])
                    f.write("id: " + id_pkm + '\n')
                    f.write(str("name: " + pokemon['name']) + '\n')
                    if len(pokemon['types']) == 1:
                        f.write(str("type: " + pokemon['types'][0]) + '\n')
                    elif len(pokemon['types']) == 2:
                        f.write(str("types: " + pokemon['types'][0] + "/" + pokemon['types'][1]) + '\n')
                    f.write(str("__________________") + '\n')

            i += 1
        print("Your team had been successfully created on", team[0] + ".txt")


def main():
    parser = argparse.ArgumentParser(
        description="pokedex.py is a script wich allows you to get informations about pokemon and even build your "
                    "team !")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--list", help="to access the list of all pokemon.", action="store_true")
    group.add_argument("-i", "--info",
                       help="to access the data about an individual pokemon. Needs to be followed by a pokemon name.")
    group.add_argument("-w", "--weakness",
                       help="to access the weaknesses of an individual pokemon. Needs to be followed by a pokemon name.")
    group.add_argument("-r", "--resistance",
                       help="to access the resistances of an individual pokemon. Needs to be followed by a pokemon name.")
    group.add_argument("-p", "--picture",
                       help="to display the picture of an individual pokemon in browser. Needs to be followed by a pokemon name.")
    group.add_argument("-t", "--team", nargs='+', help="Write a team of 6 pokemon on a file.txt. Required arguments: "
                                                       "filename / pkm1 / pkm2 / pkm3 / pkm4 / pkm5 / pkm6 /")

    arguments = parser.parse_args()

    if arguments.list:
        list_option()
    elif arguments.info is not None:
        info_option(arguments.info.title())
    elif arguments.weakness is not None:
        weakness_option(arguments.weakness.title())
    elif arguments.resistance is not None:
        resistance_option(arguments.resistance.title())
    elif arguments.picture is not None:
        picture_option(arguments.picture.title())
    elif arguments.team is not None:
        team_option(arguments.team)


if __name__ == '__main__':
    main()
