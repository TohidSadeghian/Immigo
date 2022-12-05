from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from feeds.models import News
from .serializers import NewsSerializer
from common.paginations import CustomPagination


class NewsViewset(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet
                ):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = CustomPagination


