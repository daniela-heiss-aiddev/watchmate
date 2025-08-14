from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
###Watchlist Serializers###
class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'

###Streaming Platform Serializers###
class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-list-details'
    # )
    class Meta:
        model = StreamingPlatform
        fields = '__all__'