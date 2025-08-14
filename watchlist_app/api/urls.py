from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamingPlatformListAV, StreamingPlatformDetailAV

urlpatterns = [
    ###Watchlist API URLs###
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-list-details'),
    ###Streaming Platform API URLs###
    path('stream/', StreamingPlatformListAV.as_view(), name='streamingplatform-list'),
    path('stream/<int:pk>', StreamingPlatformDetailAV.as_view(), name='streamingplatform-detail'),
]