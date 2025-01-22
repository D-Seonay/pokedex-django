import random
from .models import Team

def simulate_battle(team1, team2):
    score1 = sum(
        pokemon.attack + pokemon.hp + pokemon.defense + 
        pokemon.special_attack + pokemon.special_defense + pokemon.speed
        for pokemon in team1.pokemons.all()
    )
    score2 = sum(
        pokemon.attack + pokemon.hp + pokemon.defense + 
        pokemon.special_attack + pokemon.special_defense + pokemon.speed
        for pokemon in team2.pokemons.all()
    )

    score1 += random.randint(-50, 50) 
    score2 += random.randint(-50, 50)

    if score1 > score2:
        return team1
    elif score2 > score1:
        return team2
    return None 
