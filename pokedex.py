import json
import sys
import textwrap
import argparse


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


def commands(user_input, arg2):
    if user_input == "help":
        help_option()
    elif user_input == "list":
        list_option()
    elif user_input == "exit":
        exit_option()
    elif user_input == "info":
        info_option(arg2)
    elif user_input == "descript":
        description_option(arg2)
    elif user_input == "type":
        type_option(arg2)
    else:
        print("Invalid command")
        help_option()


def main():
    parser = argparse.ArgumentParser(
        description="pokedex.py is a script wich allows you to get informations about pokemon and even build your "
                    "team !")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--list", help="to access the list of all pokemon.", action="store_true")
    group.add_argument("-i", "--info",
                       help="to access the data about an individual pokemon. Needs to be followed by a pokemon name.")

    arguments = parser.parse_args()

    if arguments.list:
        list_option()
    elif arguments.info is not None:
        info_option(arguments.info.title())


if __name__ == '__main__':
    main()
