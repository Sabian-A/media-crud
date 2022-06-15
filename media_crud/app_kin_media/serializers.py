from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Track, Album, Artist
#from product.serializers import ProductSerializer


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['track_id','track_name','track_description', 'track_file']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True,read_only=False, required=False)

    class Meta:
        model = Album
        fields = [ 'album_id', 'album_name', 'tracks',]


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True,read_only=False, required=False)
    #tracks = TrackSerializer(many=True,read_only=False, required=False)

    class Meta:
        model = Artist
        fields = ['artist_id', 'artist_name', 'albums',]

    def create(self, validated_data):
        albums_data = validated_data.pop('albums')
        album = Artist.objects.create(**validated_data)
        for album_data in albums_data:
            tracks_data = album_data.pop('tracks')
            album = Album.objects.create(artist_id=album, **album_data)
            #for track in tracks:
                #Track.creat(album_id=album, **track) 
            for track_data in tracks_data:
                Track.objects.create(album_id=album,**track_data)
        return album
    
    
    
#####################################################################################

    """def update(self, instance, validated_data):
        albums_data = validated_data.pop('albums')
        orders = instance.albums.all()
        orders = list(orders)
        instance.track_name= validated_data.get('track_name', instance.track_name)
        instance.track_file= validated_data.get('track_file', instance.track_file)
        instance.save()

        for album_data in request_orders_data:
            request_order_items_data = request_order_data.pop('request_order_itemss')
            items = instance.request_orders.get().request_order_itemss.all()
            items = list(items)
            for request_order_item_data in request_order_items_data:
                item = items.pop(0)
                item.product_id = request_order_item_data.get('product_id', item.product_id)
                item.qty = request_order_item_data.get('qty', item.qty)
                item.save()
            order = orders.pop(0)
            order.position = request_order_data.get('position', order.position)
            order.destination = request_order_data.get('destination', order.destination)
            order.order_ref = request_order_data.get('order_ref', order.order_ref)
            order.save()
        return instance"""
