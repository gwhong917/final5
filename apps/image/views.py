from django.views import View
from django.http import HttpResponse, JsonResponse
from .serializers import CreateSerializer
from rest_framework.generics import (CreateAPIView)
from rest_framework.response import Response
from rest_framework import status
from .models import Post


class PostCreateAPIView(CreateAPIView):
    def post(self, request, format=None):
        serializer_class = CreateSerializer(data=request.data)
        print(request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


