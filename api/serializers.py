from rest_framework import serializers

from django.contrib.auth.models import User
from app.models import Profile, Item, ItemLike, ItemComment


class ProfileSerializer(serializers.ModelSerializer):
    get_mugshot_url = serializers.Field(source='get_mugshot_url')

    class Meta:
        model = Profile
        fields = ('nickname', 'notice_at', 'get_mugshot_url')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        queryset = User.objects.exclude(pk=-1)
        fields = ('id', 'username', 'profile')


class ItemLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemLike


class ItemCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ItemComment
        fields = ('id', 'user', 'text')


class ItemSerializer(serializers.ModelSerializer):
    likes = serializers.RelatedField(many=True)
    comments = ItemCommentSerializer(required=False)

    class Meta:
        model = Item
