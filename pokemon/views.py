from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon, Team, Battle
from .forms import TeamForm
from .utils import simulate_battle


def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, "pokemon_list.html", {"pokemons": pokemons})

def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, "pokemon_detail.html", {"pokemon": pokemon})

def team_list(request):
    teams = Team.objects.all()
    return render(request, "team_list.html", {"teams": teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, "pokemon/team_detail.html", {"team": team})
    
def team_create(request):
    team = Team.objects.create()
    pokemons = Pokemon.objects.all()
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect("team_detail", team_id=team.id)
    else:
        form = TeamForm()
    
    return render(request, "pokemon/team_form.html", {"form": form, "pokemons": pokemons, "team": team})

def add_pokemon_to_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "POST":
        pokemon_id = request.POST.get("pokemon_id")
        pokemon = get_object_or_404(Pokemon, id=pokemon_id)
        team.pokemons.add(pokemon)
    return redirect("team_detail", team_id=team.id)

def team_edit(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    pokemons = Pokemon.objects.all()
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect("team_detail", {"team": team, "pokemons": pokemons}, team_id=team.id)
    else:
        form = TeamForm(instance=team)
    
    return render(request, "pokemon/team_form.html", {"form": form, "pokemons": pokemons, "team": team})

def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "POST":
        team.delete()
        return redirect("team_list")

    return render(request, "pokemon/team_confirm_delete.html", {"team": team})

def battle_selection_view(request):
    teams = Team.objects.all()
    return render(request, "pokemon/battle_selection.html", {"teams": teams})

def battle_list(request):
    battles = Battle.objects.all().order_by("-created_at")
    return render(request, "pokemon/battle_list.html", {"battles": battles})

def battle_start(request, team1_id, team2_id):
    team1 = get_object_or_404(Team, id=team1_id)
    team2 = get_object_or_404(Team, id=team2_id)

    winner = simulate_battle(team1, team2)
    
    battle = Battle.objects.create(trainer1=team1, trainer2=team2, winner=winner)

    return redirect("battle_detail", battle_id=battle.id)

def battle_detail(request, battle_id):
    battle = get_object_or_404(Battle, id=battle_id)
    return render(request, "pokemon/battle_detail.html", {"battle": battle})