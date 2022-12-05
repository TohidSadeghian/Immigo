from django.db import models
from django.utils.translation import gettext_lazy as _
from common.basemodels import BaseModel
from .utils import news_image


class News(BaseModel):
    """
    Model for storing crawled news data 
    """
    title = models.CharField(_("title"), max_length=500, blank=True, null=True)
    url = models.CharField(_("url"), max_length=500, blank=True)
    content = models.TextField(_("content"), blank=True)
    summary = models.TextField(_("summary"), blank=True)
    image = models.ImageField(_("image"), upload_to=news_image, blank=True, null=True)
    date_published = models.CharField(_("date_published"), max_length=50, blank=True, null=True)
    author = models.CharField(_("author"), max_length=500)

    def __str__(self):
        return f'{self.title}'
    