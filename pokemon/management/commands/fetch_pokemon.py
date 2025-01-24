import requests
from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type

class Command(BaseCommand):
    help = "Fetch Pokémon data from PokeAPI"

    def handle(self, *args, **kwargs):
        api_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(api_url)
        data = response.json()
        
        for pokemon_data in data['results']:
            details = requests.get(pokemon_data['url']).json()
            
            cry_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{details['id']}.ogg"
            
            pokemon, created = Pokemon.objects.update_or_create(
                name=details['name'],
                defaults={
                    'sprite': details['sprites']['front_default'],
                    "number": details['id'],
                    'height': details['height'],
                    'weight': details['weight'],
                    'hp': details['stats'][0]['base_stat'],
                    'attack': details['stats'][1]['base_stat'],
                    'defense': details['stats'][2]['base_stat'],
                    'special_attack': details['stats'][3]['base_stat'],
                    'special_defense': details['stats'][4]['base_stat'],
                    'speed': details['stats'][5]['base_stat'],
                    'cry_url': cry_url,
                }
            )
            
            pokemon_types = [t['type']['name'] for t in details['types']]
            types_objects = []
            for type_name in pokemon_types:
                type_obj, created = Type.objects.get_or_create(name=type_name)
                types_objects.append(type_obj)

            # Affectation des types après la création ou mise à jour du Pokémon
            pokemon.types.set(types_objects)

        self.stdout.write(self.style.SUCCESS("Pokémon data fetched successfully!"))
