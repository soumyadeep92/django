from django.shortcuts import render
from .models import Song,Singer
from .serializers import SongSerializer,SingerSerializer
from rest_framework import viewsets

# Create your views here.
class SongList(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer

class SingerList(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer