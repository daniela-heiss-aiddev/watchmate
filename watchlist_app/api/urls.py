from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamingPlatformListAV, StreamingPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    ###Watchlist API URLs###
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-list-details'),
    ###Streaming Platform API URLs###
    path('stream/', StreamingPlatformListAV.as_view(), name='streamingplatform-list'),
    path('stream/<int:pk>', StreamingPlatformDetailAV.as_view(), name='streamingplatform-detail'),

    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]