from rest_framework import serializers

from webapp.models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'author', 'user']
        read_only_fields = ['author', 'user']
