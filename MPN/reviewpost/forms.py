from django.forms import ModelForm
from .models import *

class Reviewpostform(ModelForm):
    class Meta:
        model = Reviewpost
        fields = ('content_name', 'content', 'photos')

class Commentpostform(ModelForm):
    class Meta:
        model = ReviewComment
        fields = ('comment',)