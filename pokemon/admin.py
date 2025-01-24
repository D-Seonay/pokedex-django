from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Pokemon, Team, Battle
from .forms import TeamForm

@login_required
def team_create(request):
    pokemons = Pokemon.objects.all()
    form = TeamForm(request.POST or None)
    team = Team.objects.filter(user=request.user).first()  

    if form.is_valid():
        team = form.save()
        selected_pokemons = request.POST.getlist('pokemons') 
        for pokemon_id in selected_pokemons:
            pokemon = Pokemon.objects.get(id=pokemon_id)
            team.pokemons.add(pokemon)  
        return redirect('team_detail', team.id)

    return render(request, 'pokemon/team_form.html', {'form': form, 'pokemons': pokemons, 'team': team}) 

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'get_types', 'height', 'weight')  
    search_fields = ('name',)

    def get_types(self, obj):
        """ Affiche les types sous forme de texte séparé par des virgules """
        return ", ".join([t.name for t in obj.types.all()])
    
    get_types.short_description = "Types"  
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = ('trainer1', 'trainer2', 'winner', 'created_at')
    search_fields = ('trainer1__username', 'trainer2__username', 'winner__username')  
