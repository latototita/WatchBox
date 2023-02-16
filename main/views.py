from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import *
import random
from django.shortcuts import render, HttpResponse
import os
# defining function
def index(request):
    # checking whether request.method is post or not
    movies=File.objects.all()
    context={'movies':movies}
    return render(request, 'index.html',context)

def movie_detail(request, id):
    i = File.objects.get(id=id)
    return render(request, 'watchmv.html', {'i': i})

def stream_video(request, id):
    video = File.objects.get(id=id)
    file_path = video.file.path
    video_file = open(file_path, 'rb')
    response = HttpResponse(video_file, content_type='video/mp4')
    response['Content-Disposition'] = 'inline; filename="video.mp4"'
    return response


def download(request, path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404



# series/views.py



def series_list(request):
    movies = Series.objects.all()
    return render(request, 'index.html', {'movies': movies})



def series_detail(request, series_id):
    series = Series.objects.get(id=series_id)
    episodes = Episode.objects.filter(series=series)
    return render(request, 'detail.html', {'series': series, 'episodes': episodes})



def episode_download(request, episode_id):
    episode = Episode.objects.get(id=episode_id)
    file = episode.episode_file
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response
from itertools import chain
'''
from django.db.models import QuerySet

def concatenate_querysets(qs1, qs2):
    if not isinstance(qs1, QuerySet) or not isinstance(qs2, QuerySet):
        raise TypeError("Both arguments must be querysets.")
    return list(chain(qs1, qs2))
    '''
def Kdrama(request):
    # checking whether request.method is post or not
    movies=File.objects.filter(is_kdrama=True)
    movies1=Series.objects.filter(is_kdrama=True)
    movies = list(chain(movies1, movies))
    #movies = concatenate_querysets(movies, movies1)
    print(movies)
    #movies=random.sample(movies, len(movies))
    context={'movies':movies}
    return render(request, 'index.html',context)
def Anime(request):
    # checking whether request.method is post or not
    movies=File.objects.filter(is_anime=True)
    movies1=Series.objects.filter(is_anime=True)
    movies = list(chain(movies1, movies))
    #movies = concatenate_querysets(movies, movies1)
    print(movies)
    #movies=random.sample(movies, len(movies))
    context={'movies':movies}
    return render(request, 'index.html',context)
def Animation(request):
    # checking whether request.method is post or not
    movies=File.objects.filter(is_animation=True)
    movies1=Series.objects.filter(is_animation=True)
    movies = list(chain(movies1, movies))
    #movies = concatenate_querysets(movies, movies1)
    print(movies)
    #movies=random.sample(movies, len(movies))
    context={'movies':movies}
    return render(request, 'index.html',context)


def episode_stream(request, id):
    episode = Episode.objects.get(id=id)
    file_path = episode.episode_file.path

    response = HttpResponse()
    response['Content-Type'] = 'video/mp4'
    response['Content-Length'] = os.path.getsize(file_path)

    with open(file_path, 'rb') as f:
        response.write(f.read())

    return response