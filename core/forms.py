from django import forms
from .models import *
class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ("title", "description", "song")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SongUploadForm, self).__init__(*args, **kwargs)

    def clean_user(self):
        return self.user