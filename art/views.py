from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Artwork, Artist, Ledger
from .forms import ArtworkForm, ArtistForm
import fractions

@login_required
def art_list(request):
	arts = Artwork.objects.order_by('artist')
	return render(request, 'art/art_list.html', {'arts': arts})

@login_required
def artwork_detail(request, pk):
	art = get_object_or_404(Artwork, pk=pk)
	return render(request, 'art/artwork_detail.html', {'art': art})

@login_required
def artwork_new(request):
	if request.method == "POST":
		form = ArtworkForm(request.POST)
		if form.is_valid():
			art = form.save(commit=False)
			art.artwork_ts = timezone.now()
			art.save()
			return redirect('artwork_list', pk=art.pk)
		else:
			form = ArtworkForm()
		return render(request, 'art/artwork_edit.html', {'form': form})
	form = ArtworkForm()
	return render(request, 'art/artwork_edit.html', {'form': form})

@login_required
def artwork_edit(request, pk):
    art = get_object_or_404(Artwork, pk=pk)
    if request.method == "POST":
        form = ArtworkForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.artwork_ts = timezone.now()
            art.save()
            return redirect('artwork_list', pk=art.pk)
    else:
        form = ArtworkForm(instance=art)
    return render(request, 'art/artwork_edit.html', {'form': form})

@login_required
def artist_list(request):
	artists = Artist.objects.order_by('ln')
	return render(request, 'art/artist_list.html',{'artists': artists})

@login_required
def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.artist_published_ts = timezone.now()
            artist.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'art/artist_edit.html', {'form': form})

@login_required
def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.artist_published_ts = timezone.now()
            artist.save()
            return redirect('artist_list')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'art/artist_edit.html', {'form': form})


@login_required
def ledger_list(request):
	ledgers = Ledger.objects.order_by('name')
	return render(request, 'art/ledger_list.html',{'ledgers': ledgers})
