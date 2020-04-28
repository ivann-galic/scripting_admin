import json
import sys
import textwrap


def help_option():
    print("** HELP SECTION **")
    print("pokedex.py is a script wich allows you to get informations about pokemon and even build your team !")
    print("Please enter:")
    print("help    to display the avaible commands\n"
          "list    to access the list of all pokemon\n"
          "exit    to quit the program\n")


def list_option(dictionary):
    print("** LIST OF POKEMON **")
    for pokemon in dictionary:
        print(pokemon['pkdx_id'], pokemon['name'])
    print("")


def test(dictionary):
    for pokemon in dictionary:
        print("id: ", pokemon['pkdx_id'])
        print("name: ", pokemon['name'])
        print("description: ", "\n".join(textwrap.wrap(pokemon['description'], 160)))
        if len(pokemon['types']) == 1:
            print("type: ", pokemon['types'][0])
        elif len(pokemon['types']) == 2:
            print("types: ", pokemon['types'][0], "/", pokemon['types'][1])
        for key in pokemon.keys():
            if key == 'evolutions':
                try:
                    if len(pokemon['evolutions']) == 1:
                        print("Evolves by", pokemon['evolutions'][0]['method'].replace("_", " "), "to", pokemon['evolutions'][0]['to'])
                    elif len(pokemon['evolutions']) > 1:
                        print("This pokemon can evolve to", len(pokemon['evolutions']), "different pokemon:")
                        i = 0
                        while i < len(pokemon['evolutions']):
                            print("Evolves by", pokemon['evolutions'][i]['method'].replace("_", " "), "to", pokemon['evolutions'][i]['to'])
                            i += 1
                except IndexError:
                    continue
    print("")


def info_option(dictionary):
    pokemon_name = input("Please enter a pokemon:\n").lower()
    for pokemon in dictionary:
        if pokemon['name'] == pokemon_name:
            print(pokemon['pkdx_id'], pokemon['name'])
        else:
            print("echec")
    print("")


def exit_option():
    print("Bye and gotta catch'em all !")
    sys.exit()


def commands(data_dict):
    user_input = ""
    while user_input != "exit":
        user_input = input("Please enter a command:\n")
        if user_input == "help":
            help_option()
        elif user_input == "list":
            list_option(data_dict)
        elif user_input == "exit":
            exit_option()
        elif user_input == "info":
            info_option(data_dict)
        elif user_input == "test":
            test(data_dict)
        else:
            print("Invalid command")
            help_option()


def main():
    with open('pokemon.json') as json_pokemon:
        data_dict = json.load(json_pokemon)
    help_option()
    commands(data_dict)


if __name__ == '__main__':
    main()
