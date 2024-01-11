from django.urls import path, include

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailsAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchListDetailAV.as_view(), name="movie-details"),
    path("stream/", StreamPlatformListAV.as_view(), name="stream-platform"),
    path("stream/<int:pk>", StreamPlatformDetailsAV.as_view(), name="streamplatform-detail"),

]
