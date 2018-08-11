from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
	class Meta:
		model = Artwork
		fields = ('artwork_prid_a', 'artist', 'artwork_title', 'artwork_yyyy_a',)