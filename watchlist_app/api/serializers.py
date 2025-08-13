from rest_framework import serializers
from watchlist_app.models import Movie

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'