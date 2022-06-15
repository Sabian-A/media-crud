from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework import status

from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from .models import Artist, Album, Track
#from .serializers import AlbumSerializer
#from .models import Album
#from .serializers import TrackSerializer
#from .models import Track
from rest_framework import generics


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    


# class ArtistView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ArtistSerializer
#     queryset = Artist.objects.all()
    


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer



# class AlbumView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AlbumSerializer
#     queryset = Album.objects.all()



class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer 
    


# class TrackView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TrackSerializer
#     queryset = Track.objects.all()
    





