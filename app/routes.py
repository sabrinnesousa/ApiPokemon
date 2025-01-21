from app import app
from flask import render_template
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/temporadas')
def temporadas():
    return render_template('temporadas.html')

@app.route('/pikachu')
def pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/25/"
    response = requests.get(url)
    data = response.json()
    
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'] / 10,  # Convert meters to centimeters
        'weight': data['weight'] / 1000,  # Convert kg to grams
        'category': data.get('species', {}).get('genus', 'Unknown'),
        'abilities': [ability['ability']['name'] for ability in data.get('abilities', [])],
        'types': [type_['type']['name'] for type_ in data.get('types', [])]
    }
    
    return render_template('pikachu.html', pokemon=pokemon)

@app.route("/squirtle")
def squirtle():
    url = "https://pokeapi.co/api/v2/pokemon/7/"
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'] / 10,  # Convert meters to centimeters
        'weight': data['weight'] / 1000,  # Convert kg to grams
        'category': data.get('species', {}).get('genus', 'Unknown'),
        'abilities': [ability['ability']['name'] for ability in data.get('abilities', [])],
        'types': [type_['type']['name'] for type_ in data.get('types', [])]
    }
    return render_template('squirtle.html', pokemon=pokemon)

@app.route("/clefairy")
def clefairy():
    url = "https://pokeapi.co/api/v2/pokemon/36/"
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'] / 10,  # Convert meters to centimeters
        'weight': data['weight'] / 1000,  # Convert kg to grams
        'category': data.get('species', {}).get('genus', 'Unknown'),
        'abilities': [ability['ability']['name'] for ability in data.get('abilities', [])],
        'types': [type_['type']['name'] for type_ in data.get('types', [])]
    }
    return render_template ('clefairy.html', pokemon=pokemon)

@app.route("/wigglytuff")
def wigglytuff():
    url = "https://pokeapi.co/api/v2/pokemon/40/"
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'] / 10,  # Convert meters to centimeters
        'weight': data['weight'] / 1000,  # Convert kg to grams
        'category': data.get('species', {}).get('genus', 'Unknown'),
        'abilities': [ability['ability']['name'] for ability in data.get('abilities', [])],
        'types': [type_['type']['name'] for type_ in data.get('types', [])]
    }
    return render_template('wigglytuff.html', pokemon=pokemon)

@app.route('/charmander')
def charmander():
    url = "https://pokeapi.co/api/v2/pokemon/4/"
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'] / 10,  # Convert meters to centimeters
        'weight': data['weight'] / 1000,  # Convert kg to grams
        'category': data.get('species', {}).get('genus', 'Unknown'),
        'abilities': [ability['ability']['name'] for ability in data.get('abilities', [])],
        'types': [type_['type']['name'] for type_ in data.get('types', [])]
    }
    return render_template('charmander.html', pokemon=pokemon)

@app.route('/psyduck')
def psyduck():
    url = "https://pokeapi.co/api/v2/pokemon/psyduck"
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'] / 10,  # Convert meters to centimeters
        'weight': data['weight'] / 1000,  # Convert kg to grams
        'category': data.get('species', {}).get('genus', 'Unknown'),
        'abilities': [ability['ability']['name'] for ability in data.get('abilities', [])],
        'types': [type_['type']['name'] for type_ in data.get('types', [])]
    }
    return render_template('psyduck.html', pokemon=pokemon)
