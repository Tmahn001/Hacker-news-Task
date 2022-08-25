from rest_framework import serializers
from .models import NewsID, News

class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsID
        fields = ('hackernews',)

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "hackernews_id", "time", "category","post_url", "author", "path")