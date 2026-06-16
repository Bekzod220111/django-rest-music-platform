from rest_framework.serializers import ModelSerializer
from apps.users.models import FavouritePlaylist
from rest_framework.exceptions import ValidationError

class FavouritePlaylistListSerializers(ModelSerializer):

    class Meta:
        model = FavouritePlaylist
        fields = '__all__'

class FavouritePlaylistCreateSerializers(ModelSerializer):

    class Meta:
        model = FavouritePlaylist
        fields = '__all__'

    def validate_playlist(self, playlist):

        favourite = FavouritePlaylist.objects.filter(user=self.user, playlist=playlist)
        if favourite.exists():
            raise ValidationError('This music already exists in your favourite list.')
        elif  not playlist.is_public:
            raise ValidationError('You can not add this playlist to your favourite.')
        return playlist


