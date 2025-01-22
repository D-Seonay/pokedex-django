from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('<int:pk>/', views.pokemon_detail, name='pokemon_detail'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/add_pokemon/', views.add_pokemon_to_team, name='add_pokemon_to_team'),
    path('teams/<int:team_id>/edit/', views.team_edit, name='team_edit'),
    path('teams/<int:team_id>/delete/', views.team_delete, name='team_delete'),
    path('battles/', views.battle_list, name='battle_list'),
    path('battles/select/', views.battle_selection_view, name='battle_selection'),
]
