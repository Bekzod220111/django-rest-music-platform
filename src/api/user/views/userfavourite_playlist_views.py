from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import userfavourite_playlist_serializers
from rest_framework import status
from rest_framework.response import Response
from apps.users.models import FavouritePlaylist

class FavouritePlaylistListApiView(ListAPIView):
    queryset = FavouritePlaylist.objects.all()
    serializer_class = userfavourite_playlist_serializers.FavouritePlaylistListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user.request.user)

class FavouritePlaylistCreateAPIView(CreateAPIView):
    queryset = FavouritePlaylist.objects.all()
    serializer_class = userfavourite_playlist_serializers.FavouritePlaylistCreateSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        data['user'] = request.user.id
        ser = self.serializer_class(data=data)
        ser.user = request.user
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response({
            "msg": "favourite playlist added successfully",
            "data": ser.data
        }, status=status.HTTP_201_CREATED)




class FavouritePlaylistDestroyAPIView(DestroyAPIView):
    queryset = FavouritePlaylist.objects.all()
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            status_code = status.HTTP_204_NO_CONTENT
        else:
            status_code = status.HTTP_404_NOT_FOUND
        return Response(status=status_code)