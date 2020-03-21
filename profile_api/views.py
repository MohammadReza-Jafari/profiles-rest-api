from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer


class HelloApiView(APIView):
    serializer_class = HelloSerializer

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
            name = ser.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message}, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """Update an object"""
        return Response({'message': 'put'})

    def patch(self,request):
        """Partial update an object"""
        return Response({'message': 'patch'})

    def delete(self,request):
        """Delete an object"""
        return Response({'message': 'delete'})
