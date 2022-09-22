from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Article
from .serializers import ArticleSerializers


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializers(article)
            return Response(serializer.data)
        else:
            articles = Article.objects.all()
            serializers = ArticleSerializers(articles, many=True)
            return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializers(data=request.data, instance=article)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        Article.delete(article)
        return Response(status=status.HTTP_204_NO_CONTENT)
