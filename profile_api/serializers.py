from rest_framework import serializers
from profile_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes name field for hello api view"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Create a User profile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes a profile feed item"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'created_on', 'status_text')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
