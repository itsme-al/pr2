from django.urls import path
from . import views


urlpatterns = [
	path('', views.ledger_list, name='ledger_list'),
	path('art/', views.art_list, name='art_list'),
	path('art/<int:pk>/', views.artwork_detail, name='artwork_detail'),
	path('art/new/', views.artwork_new, name='artwork_new'),
	path('art/<int:pk>/edit/', views.artwork_edit, name='artwork_edit'),
	path('artists/', views.artist_list, name='artist_list'),
	path('artist/new/', views.artist_new, name='artist_new'),
	path('artist/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
]