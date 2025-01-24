from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Pokemon, Team, Battle, TeamPokemon
from .forms import TeamForm
from .utils import simulate_battle


def pokemon_list(request):
    search_query = request.GET.get('search', '')
    type_filter = request.GET.get('type', '')

    pokemons = Pokemon.objects.all()

    if search_query:
        pokemons = pokemons.filter(name__icontains=search_query)

    if type_filter:
        pokemons = pokemons.filter(types__name__iexact=type_filter)

    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, pk):
    search_query = request.GET.get('search', '')
    type_filter = request.GET.get('type', '')

    pokemons = Pokemon.objects.all()

    if search_query:
        pokemons = pokemons.filter(name__icontains=search_query)

    if type_filter:
        pokemons = pokemons.filter(types__name__iexact=type_filter)

    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, "pokemon_detail.html", {"pokemon": pokemon})

def team_list(request):
    teams = Team.objects.all()
    return render(request, "team/team_list.html", {"teams": teams})

def team_create(request):
    team = Team.objects.create(name="Nouvelle équipe")
    return redirect("team_detail", team_id=team.id)

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    pokemons = Pokemon.objects.all()
    
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_detail', team_id=team.id)
    else:
        form = TeamForm(instance=team)
    
    return render(request, 'team/team_detail.html', {'form': form, 'pokemons': pokemons, 'team': team})

def update_team_name(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == "POST":
        new_name = request.POST.get('name')

        if new_name:
            team.name = new_name
            team.save()
            return JsonResponse({"success": True, "team_name": team.name})
        else:
            return JsonResponse({"success": False, "error": "Nom de l'équipe invalide."})

    return JsonResponse({"success": False, "error": "Requête invalide."})

def add_pokemon_ajax(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == "POST":
        pokemon_id = request.POST.get("pokemon_id")
        pokemon = get_object_or_404(Pokemon, id=pokemon_id)

        if team.pokemons.count() >= 6:
            return JsonResponse({"success": False, "error": "L'équipe ne peut contenir que 6 pokémons maximum."})

        order = team.pokemons.count() + 1
        team_pokemon = TeamPokemon.objects.create(team=team, pokemon=pokemon, order=order)

        pokemon_types = ", ".join([type.name for type in pokemon.types.all()])

        return JsonResponse({
            "success": True,
            "pokemon_id": pokemon.id,
            "pokemon_name": pokemon.name,
            "pokemon_sprite": pokemon.sprite,
            "pokemon_types": pokemon_types,
            "order": order
        })

    return JsonResponse({"success": False, "error": "Requête invalide."})

def remove_pokemon_ajax(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == "POST":
        pokemon_id = request.POST.get("pokemon_id")
        pokemon = get_object_or_404(Pokemon, id=pokemon_id)

        team_pokemon = TeamPokemon.objects.filter(team=team, pokemon=pokemon).first()

        if not team_pokemon:
            return JsonResponse({"success": False, "error": "Pokémon non trouvé dans l'équipe."})

        team_pokemon.delete()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Requête invalide."})

def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "POST":
        team.delete()
        return redirect('team_list')
    return render(request, "team/team_confirm_delete.html", {"team": team})

def battle_selection_view(request):
    teams = Team.objects.all()
    return render(request, "battle_selection.html", {"teams": teams})

def battle_list(request):
    battles = Battle.objects.all().order_by("-created_at")
    return render(request, "battle_list.html", {"battles": battles})

def battle_start(request, team1_id, team2_id):
    team1 = get_object_or_404(Team, id=team1_id)
    team2 = get_object_or_404(Team, id=team2_id)

    winner = simulate_battle(team1, team2)
    
    battle = Battle.objects.create(trainer1=team1, trainer2=team2, winner=winner)

    return redirect("battle_detail", battle_id=battle.id)

def battle_detail(request, battle_id):
    battle = get_object_or_404(Battle, id=battle_id)
    return render(request, "battle_detail.html", {"battle": battle})
