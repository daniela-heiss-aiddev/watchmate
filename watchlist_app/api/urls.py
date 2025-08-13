from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watch-list-details'),
]
