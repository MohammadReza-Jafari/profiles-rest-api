from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
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
