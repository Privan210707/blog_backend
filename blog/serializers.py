from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class SignupSerializer(serializers.ModelSerializer):

    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        bio = validated_data.pop('bio', '')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        Profile.objects.create(
            user=user,
            bio=bio
        )

        return user