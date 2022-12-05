from rest_framework import serializers
from feeds.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "url", "content", "summary", "image", "date_published", "author")
