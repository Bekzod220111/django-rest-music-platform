from rest_framework.serializers import ModelSerializer
from apps.music.models import Playlist

class PlaylistListSerializers(ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistCreateSerializers(ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ['saves_count', 'musics_count']

