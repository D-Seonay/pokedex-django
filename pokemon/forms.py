from django import forms
from .models import Team, Pokemon

class TeamForm(forms.ModelForm):
    pokemons = forms.ModelMultipleChoiceField(
        queryset=Pokemon.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Team
        fields = ["name", "pokemons"]
    
    def clean_pokemons(self):
        pokemons = self.cleaned_data.get('pokemons')
        if len(pokemons) > 6:
            raise forms.ValidationError('You cannot add more than 6 Pokémon to your team.')
        return pokemons
