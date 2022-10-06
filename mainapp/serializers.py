from rest_framework import serializers

from mainapp.models import (Post, Like, Unlike)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user', 'post', 'date'
        )
        read_only_fields = ('post', 'user', 'date',)


class UnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unlike
        fields = (
            'user', 'post', 'date'
        )
        read_only_fields = ('post', 'user', 'date',)


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(read_only=True, many=True)
    unlikes = LikeSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            'id', 'name', 'user', 'likes_amount', 'unlikes_amount', 'likes', 'unlikes'
        )
