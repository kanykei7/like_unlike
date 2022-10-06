from rest_framework.routers import DefaultRouter as DR

from mainapp.views import PostViewSet

router = DR()

router.register('posts', PostViewSet, basename='posts')
urlpatterns = []

urlpatterns += router.urls
