from django.urls import path
from . import views


urlpatterns = [
	path('', views.art_list, name='art_list'),
	path('art/<int:pk>/', views.artwork_detail, name='artwork_detail'),
	path('art/new/', views.artwork_new, name='artwork_new'),
	path('art/<int:pk>/edit/', views.artwork_edit, name='artwork_edit'),
	path('artists/', views.artist_list, name='artist_list'),
]