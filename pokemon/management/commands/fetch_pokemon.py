import requests
from django.core.management.base import BaseCommand
from pokemon.models import Pokemon

class Command(BaseCommand):
    help = "Fetch Pokémon data from PokeAPI"

    def handle(self, *args, **kwargs):
        api_url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Récupère les 50 premiers Pokémon
        response = requests.get(api_url)
        data = response.json()
        
        for pokemon_data in data['results']:
            details = requests.get(pokemon_data['url']).json()
            Pokemon.objects.update_or_create(
                name=details['name'],
                defaults={
                    'sprite': details['sprites']['front_default'],
                    'types': ", ".join(t['type']['name'] for t in details['types']),
                    'height': details['height'],
                    'weight': details['weight']
                }
            )
        self.stdout.write(self.style.SUCCESS("Pokémon data fetched successfully!"))
