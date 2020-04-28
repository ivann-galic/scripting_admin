import json
import sys


def help():
    print("** HELP SECTION **")
    print("pokedex.py is a script wich allows you to get informations about pokemon and even build your team !")
    print("Please enter:")
    print("help    to display the avaible commands\n"
          "list    to access the list of all pokemon\n"
          "exit    to quit the program\n")


def list(dictionary):
    print("** LIST OF POKEMON **")
    for pokemon in dictionary:
        print(pokemon['pkdx_id'], pokemon['name'])
    print("")

def exit():
    print("Bye and gotta catch'em all !")
    sys.exit()

def commands(data_dict):
    user_input = ""
    while user_input != "exit":
        user_input = input("Please enter a command:\n")
        if user_input == "help":
            help()
        elif user_input == "list":
            list(data_dict)
        elif user_input == "exit":
            exit()
        else:
            print("Invalid command")
            help()


def main():
    with open('pokemon.json') as json_pokemon:
        data_dict = json.load(json_pokemon)
    help()
    commands(data_dict)


if __name__ == '__main__':
    main()
