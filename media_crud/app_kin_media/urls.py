from app_kin_media.views import ArtistViewSet, AlbumViewSet, TrackViewSet
from rest_framework import routers
from rest_framework.views import APIView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.SimpleRouter()


router.register(r'artist',ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)



urlpatterns = router.urls
# urlpatterns = [
#     path('artist/', ArtistView.as_view(), name='artist'),
#     path('album/', AlbumView.as_view(), name='album'),
#     path('track/', TrackView.as_view(), name='track'),
# ]
urlpatterns = format_suffix_patterns(urlpatterns)