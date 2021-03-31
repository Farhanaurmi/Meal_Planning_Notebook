from django.forms import ModelForm
from .models import Recipepost

class Recipepostform(ModelForm):
    class Meta:
        model = Recipepost
        fields = ('title', 'recipe', 'photos')

         