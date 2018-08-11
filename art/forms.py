from django import forms
from .models import Artwork
from .models import Artist
from djfractions.forms import DecimalFractionField

class ArtworkForm(forms.ModelForm):
	class Meta:
		model = Artwork
		fields = ('prid_a', 'prid_b', 'artist', 'artwork_title', 'artwork_yyyy_a', 'size_x', 'size_y')


class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ('artist_fn', 'artist_ln', 'artist_sex', 'wiki')