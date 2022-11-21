from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .forms import SongUploadForm
from django.contrib import auth

from .models import Song




def home(request):
    blogs = Song.objects.all()
    return render(request, "index.html", {'blogs': blogs})





def createpost(request):
        if request.method == 'POST':
            if request.POST.get('songName') and request.POST.get('description') and request.POST.get('songs'):
                post=Song()
                Song.title= request.POST.get('songName')
                Song.description= request.POST.get('description')
                Song.song= request.POST.get('songs')
                post.save()
                
                return render(request, 'songs/create.html')  

        else:
                return render(request, 'songs/create.html')  







def SongUpload(request):
    if request.method == 'POST':
        song_title = request.POST['songName']
        description = request.POST['description']
        songs = request.POST['songs']
        
        insertsong = Song.objects(title=songName, description=description, song=songs)
        user.save();
        print('song inserted')
        return redirect('/')
        
    else:
        return render(request, 'songs/create.html', {'form': form})





       
    
    