from rest_framework import serializers
from watchlist_app.models import Movie, StreamingPlatform

###Watchlist Serializers###
class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

###Streaming Platform Serializers###
class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = '__all__'