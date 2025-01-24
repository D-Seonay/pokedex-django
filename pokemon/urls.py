# urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Home page (renaming to 'pokemon_list')
    path("", views.pokemon_list, name="pokemon_list"),

    # Pokemon-related URLs
    path("pokemon/<int:pk>/", views.pokemon_detail, name="pokemon_detail"),

    # Team-related URLs
    path("teams/", views.team_list, name="team_list"),
    path("teams/create/", views.team_create, name="team_create"),
    path("teams/<int:team_id>/", views.team_detail, name="team_detail"),
    path("teams/<int:team_id>/update_name/", views.update_team_name, name="update_team_name"),
    path("teams/<int:team_id>/add_pokemon/", views.add_pokemon_ajax, name="add_pokemon_ajax"),
    path("teams/<int:team_id>/remove_pokemon/", views.remove_pokemon_ajax, name="remove_pokemon_ajax"),
    path("teams/<int:team_id>/delete/", views.team_delete, name="team_delete"),

    # Battle-related URLs
    path("battles/", views.battle_list, name="battle_list"),
    path("battles/select/", views.battle_selection_view, name="battle_selection"),
    path("battles/start/<int:team1_id>/<int:team2_id>/", views.battle_start, name="battle_start"),
    path("battles/<int:battle_id>/", views.battle_detail, name="battle_detail"),
]
