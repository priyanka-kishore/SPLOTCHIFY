from flask import Flask, render_template
from PokeModel import PokeClient
app = Flask(__name__)

poke_client = PokeClient() # create instance of PokeClient class

@app.route('/')
def index():
    pokemon_list = poke_client.get_pokemon_list()
    return render_template('index.html', pokemon_list=pokemon_list)

@app.route('/pokemon/<pokemon_name>')
def pokemon_info(pokemon_name):
    pokemon_info = poke_client.get_pokemon_info(pokemon_name)
    return render_template('poke-info.html', pokemon_name=pokemon_name, pokemon_info=pokemon_info)

@app.route('/ability/<ability_name>')
def pokemon_with_ability(ability_name):
    pokemon_list = poke_client.get_pokemon_with_ability(ability_name)
    return render_template('poke-abilities.html', pokemon_list=pokemon_list, ability=ability_name)