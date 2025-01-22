from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    number = models.IntegerField(null=True, blank=True)
    sprite = models.URLField(null=True, blank=True)
    types = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    hp = models.IntegerField(null=True, blank=True)  # Exemple pour ajouter hp
    attack = models.IntegerField(null=True, blank=True)  # Exemple pour ajouter attack
    defense = models.IntegerField(null=True, blank=True)  # Exemple pour ajouter defense
    special_attack = models.IntegerField(null=True, blank=True)  # Exemple pour ajouter special_attack
    special_defense = models.IntegerField(null=True, blank=True)  # Exemple pour ajouter special_defense
    speed = models.IntegerField(null=True, blank=True)  # Exemple pour ajouter speed
    cry_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    pokemons = models.ManyToManyField(Pokemon, related_name="teams")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Battle(models.Model):
    trainer1 = models.ForeignKey(Team, related_name="battles_as_trainer1", on_delete=models.CASCADE)
    trainer2 = models.ForeignKey(Team, related_name="battles_as_trainer2", on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name="battles_won", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trainer1.name} vs {self.trainer2.name}"
