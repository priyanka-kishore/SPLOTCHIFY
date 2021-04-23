import requests

class PokeClient(object):
    def __init__(self):
        # api access stuffs
        self.sess = requests.Session()
        self.sess.headers.update({'User Agent': 'CMSC388J Spring 2021 Project 2'})
        self.base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon_list(self):
        pokemon = []
        resp = self.sess.get(f'{self.base_url}/pokemon?limit=1200')
        for poke_dict in resp.json()['results']:
            pokemon.append(poke_dict['name'])
        return pokemon
    
    def get_pokemon_info(self, pokemon):
        req = f'pokemon/{pokemon}'
        resp = self.sess.get(f'{self.base_url}/{req}')

        code = resp.status_code
        if code != 200:
            raise ValueError(f'Request failed with status code: {code} and message: '
                             f'{resp.text}')
        
        resp = resp.json()
        
        result = {}

        result['name'] = resp['name']
        result['height'] = resp['height']
        result['weight'] = resp['weight']
        result['base_exp'] = resp['base_experience']

        moves = []
        for move_dict in resp['moves']:
            moves.append(move_dict['move']['name'])
        
        result['moves'] = moves

        abilities = []
        for ability_dict in resp['abilities']:
            abilities.append(ability_dict['ability']['name'])
        
        result['abilities'] = abilities

        return result

    def get_pokemon_with_ability(self, ability):
        req = f'ability/{ability}'
        resp = self.sess.get(f'{self.base_url}/{req}')

        code = resp.status_code
        if code != 200:
            raise ValueError(f'Request failed with status code: {code} and message: '
                             f'{resp.text}')

        pokemon = []
        for poke_dict in resp.json()['pokemon']:
            pokemon.append(poke_dict['pokemon']['name'])
        
        return pokemon