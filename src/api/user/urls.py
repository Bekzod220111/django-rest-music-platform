from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views import music_views, playlist_views, userfavourite_playlist_views, userfavourite_views

router = DefaultRouter()
router.include_root_view = False

urlpatterns = [

    path('music/', music_views.MusicListApiView.as_view()),
    path('music/create/', music_views.MusicCreateAPIView.as_view()),
    path('music/detail/<int:pk>/', music_views.MusicRetrieveAPIView.as_view()),
    path('music/update/<int:pk>/', music_views.MusicUpdateAPIView.as_view()),
    path('music/delete/<int:pk>/', music_views.MusicDestroyAPIView.as_view()),

    path('playlist/', playlist_views.PlaylistListApiView.as_view()),
    path('playlist/create/', playlist_views.PlaylistCreateAPIView.as_view()),
    path('playlist/detail/<int:pk>/', playlist_views.PlaylistRetrieveAPIView.as_view()),
    path('playlist/update/<int:pk>/', playlist_views.PlaylistUpdateAPIView.as_view()),
    path('playlist/delete/<int:pk>/', playlist_views.PlaylistDestroyAPIView.as_view()),

    path('favplaylist/', userfavourite_playlist_views.FavouritePlaylistListApiView.as_view()),
    path('favplaylist/create/', userfavourite_playlist_views.FavouritePlaylistCreateAPIView.as_view()),
    path('favplaylist/delete/<int:pk>/', userfavourite_playlist_views.FavouritePlaylistDestroyAPIView.as_view()),

    path('favourite/', userfavourite_views.FavouriteListApiView.as_view()),
    path('favourite/create/', userfavourite_views.FavouriteCreateAPIView.as_view()),
    path('favourite/delete/<int:pk>/', userfavourite_views.FavouriteDestroyAPIView.as_view()),
    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]
