from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for tessting our APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for our user profile objects """

    class Meta:
        model=models.User
        fields =('id', 'email', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user"""
        user= models.User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items"""

    class Meta:
        model=models.ProfileFeedItem
        fields= ('id','user_profile','status_text','created_on',)
        extra_kwargs={'user_profile':{'read_only':True}}
