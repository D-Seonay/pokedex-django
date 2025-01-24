from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type
import requests

class Command(BaseCommand):
    help = 'Fetches Pokémon data from PokeAPI and stores it in the database'

    def handle(self, *args, **kwargs):
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        
        for i in range(1, 11):
            response = requests.get(url.format(i))
            data = response.json()

            name = data['name']
            pokemon_types = [type['type']['name'] for type in data['types']]

            types_objects = []
            for type_name in pokemon_types:
                type_obj, created = Type.objects.get_or_create(name=type_name)
                types_objects.append(type_obj)

            pokemon, created = Pokemon.objects.update_or_create(
                name=name,
                defaults={
                    'number': data['id'],
                    'sprite': data['sprites']['front_default'],
                    'height': data['height'],
                    'weight': data['weight'],
                    'hp': None,
                    'attack': None,
                    'defense': None,
                    'special_attack': None,
                    'special_defense': None,
                    'speed': None,
                    'cry_url': None,
                }
            )
            pokemon.types.set(types_objects)
            pokemon.save()

        self.stdout.write(self.style.SUCCESS('Pokémons fetched successfully!'))
