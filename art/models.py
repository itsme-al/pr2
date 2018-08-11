from django.db import models
from django.utils import timezone


class Artist(models.Model):
	SEX = (
		('F', 'Female'),
		('M', 'Male'),
		('N/A', 'N/A'),
		)
	artist_fn = models.CharField(max_length=100, verbose_name='First Name')
	artist_ln = models.CharField(max_length=200, verbose_name='Last Name')
	artist_sex = models.CharField(max_length=3, choices=SEX, null=True, verbose_name='Sex')
	artist_created_ts = models.DateTimeField(auto_now=True)
	artist_published_ts = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.artist_published_ts = timezone.now()
		self.save()

	@property
	def artist_full_name(self):
		return '{0} {1}'.format(self.artist_fn, self.artist_ln)
	
	def __str__(self):
		return self.artist_full_name

class Artwork(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Artist')
	artwork_prid_a = models.IntegerField(default=0, verbose_name='PR ID - A')
	artwork_prid_b = models.IntegerField(default=0, verbose_name='PR ID - B')
	artwork_title = models.CharField(max_length=200, verbose_name='Title')	
	artwork_yyyy_a = models.IntegerField(default=1900, verbose_name='Date')
	artwork_ts = models.DateTimeField(blank=True, null=True)
	def __str__(self):
		return self.artwork_title