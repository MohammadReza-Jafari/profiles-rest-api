from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_api import serializers, models, permissions


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        names = [
            'mohammad reza',
            'fati',
            'tanin'
        ]

        return Response({
            'message': 'Hello',
            'names': names
        })

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            name = ser.validated_data['name']
            message = f'Hello, {name}'
            return Response({'message': message}, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update an object"""
        return Response({'message': 'put'})

    def patch(self, request, pk=None):
        """Partial update an object"""
        return Response({'message': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        return Response({'message': 'hello view set'})

    def create(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            name = ser.validated_data['name']
            message = f'name = {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'message': 'retrieve'})

    def update(self, request, pk=None):
        return Response({'message': 'update'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'partial update'})

    def destroy(self, request, pk=None):
        return Response({'message': 'destroy'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating a UserProfile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user login token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnFeed, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
