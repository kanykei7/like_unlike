from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from mainapp.serializers import (Post, PostSerializer, Like, LikeSerializer, Unlike, UnlikeSerializer)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(methods=['get', ], detail=True, serializer_class=LikeSerializer)
    def likes(self, request, *args, **kwargs):
        user = request.user
        post = self.get_object()
        unlike = Unlike.objects.filter(user=user, post=post)
        like = Like.objects.filter(user=user, post=post)
        if like.exists():
            like.delete()
            return Response({"message": 'deleted'})
        elif unlike.exists():
            unlike.delete()
            Like.objects.create(user=user, post=post)
            return Response({"message": 'deleted'})
        Like.objects.create(user=user, post=post)
        return Response({"message": 'created'})

    @action(methods=['get', ], detail=True, serializer_class=UnlikeSerializer)
    def unlikes(self, request, *args, **kwargs):
        user = request.user
        post = self.get_object()
        unlike = Unlike.objects.filter(user=user, post=post)
        like = Like.objects.filter(user=user, post=post)
        if unlike.exists():
            unlike.delete()
            return Response({"message": 'deleted'})
        elif like.exists():
            like.delete()
            Unlike.objects.create(user=user, post=post)
            return Response({"message": 'deleted'})
        Unlike.objects.create(user=user, post=post)
        return Response({"message": 'created'})

    @action(methods=['get', ], detail=False, serializer_class=LikeSerializer)
    def get_date_range_likes(self, request, *args, **kwargs):
        date_from = request.query_params.get('date_from', None)
        date_to = request.query_params.get('date_to', None)
        if date_from == None or date_to == None:
            return Response({'message': 'Set date`s in query params'})
        elif date_from == None and date_to == None:
            return Response({'message': 'Set date`s in query params'})
        likes = Like.objects.filter(date__gte=date_from, date__lte=date_to).order_by('date')
        dates = []

        return Response(LikeSerializer(likes, many=True).data)


# {
#     '2022-10-06': 10,
#     '2022-10-07': 14,
# }