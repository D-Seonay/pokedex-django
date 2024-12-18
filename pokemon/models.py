from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    sprite = models.URLField()  # URL de l'image
    types = models.CharField(max_length=100)  # Liste des types
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name
