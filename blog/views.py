from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import SignupSerializer


@api_view(['GET'])
def hello_api(request):
    return Response({
        "message": "Hello! Welcome to my Blog API"
    })


@api_view(['POST'])
def signup_api(request):
    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response({
            "message": "User registered successfully",
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_201_CREATED)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )