import json




def main():


    with open('pokemon.json') as json_pokemon:
        data_dict = json.load(json_pokemon)



    for pokemon in data_dict:
        print(pokemon['pkdx_id'], pokemon['name'])
        print(pokemon['types'])
        print(pokemon['description'])
        #il ne rentre pas dans le if. JAMAIS !
        if pokemon['evolutions'] in data_dict:
            for next_pokemon in data_dict:
                print(next_pokemon['to'], next_pokemon['level'], next_pokemon['method'])




if __name__ == '__main__':
    main()