from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV, 
                                     StreamPlatformListAV, StreamPlatformDetailsAV, 
                                     ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS)

# view set routers
router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename="stream")


urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchListDetailAV.as_view(), name="movie-details"),

    path("", include(router.urls)), # view set URL


    # path("stream/", StreamPlatformListAV.as_view(), name="stream-platform"),
    # path("stream/<int:pk>", StreamPlatformDetailsAV.as_view(), name="streamplatform-detail"),


    # path("review/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),

    path("stream/<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-detail")

]
