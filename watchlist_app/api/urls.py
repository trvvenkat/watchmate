from django.urls import path, include

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailsAV, ReviewList, ReviewDetail

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchListDetailAV.as_view(), name="movie-details"),
    path("stream/", StreamPlatformListAV.as_view(), name="stream-platform"),
    path("stream/<int:pk>", StreamPlatformDetailsAV.as_view(), name="streamplatform-detail"),

    
    path("review/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail")

]
