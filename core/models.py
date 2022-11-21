from django.db import models
from time import strftime, gmtime
from utils.song_utils import generate_file_name
from accounts.models import User


def song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'songs/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name() + '.' + filename.split('.')[-1])

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Song name")
    description = models.TextField()
    song = models.FileField(upload_to=song_directory_path, max_length=500)
    # vote = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

#  class Vote(models.Model):
#     songs = models.ForeignKey(Song, on_delete=models.CASCADE)
#     voter = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title

# class VoterIp(models.Model):
#     songs = models.ForeignKey(Song, on_delete=models.CASCADE)
#     ip = models.CharField(max_length=100)
#     def __str__(self):
#         return self.ip 

