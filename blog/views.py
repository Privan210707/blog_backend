from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import SignupSerializer,ProfileSerializer
from .models import  Profile


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

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_api(request):
        profile = Profile.objects.get(user=request.user)

        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)

        if request.method == 'PUT':
            serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )