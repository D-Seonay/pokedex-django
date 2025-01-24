from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    number = models.IntegerField(null=True, blank=True)
    sprite = models.URLField(null=True, blank=True)
    types = models.ManyToManyField(Type, related_name="pokemons")
    height = models.IntegerField()
    weight = models.IntegerField()
    hp = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    special_attack = models.IntegerField(null=True, blank=True)
    special_defense = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    cry_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    pokemons = models.ManyToManyField(Pokemon, through='TeamPokemon', related_name="teams_involved")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamPokemon(models.Model):
    team = models.ForeignKey(Team, related_name='team_pokemons', on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, related_name='pokemon_teams', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pokemon.name} in {self.team.name}"

class Battle(models.Model):
    trainer1 = models.ForeignKey(Team, related_name="battles_as_trainer1", on_delete=models.CASCADE)
    trainer2 = models.ForeignKey(Team, related_name="battles_as_trainer2", on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name="battles_won", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trainer1.name} vs {self.trainer2.name}"
