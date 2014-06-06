from django.db import models

from Artist.models import Artist
from Album.models import Album
# Create your models here.

class Track(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	album = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist)
