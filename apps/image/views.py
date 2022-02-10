from django.views import View
from django.http import HttpResponse, JsonResponse
from .serializers import CreateSerializer
from rest_framework.generics import (CreateAPIView)
from .models import Post


class PostCreateAPIView(CreateAPIView):
    serializer_class = CreateSerializer
    queryset = Post.objects.all()
