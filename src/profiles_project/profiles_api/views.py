from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiView =[
            'uses HTTP methods as function (get, post,patch, put, delete)',
            'It is similar to traditional Django View',
            'Gives you the most control over the logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!','an_apiView':an_apiView})

    def post(self, request):
        """Create a hello message with your name."""
        serializer =serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message='hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})
