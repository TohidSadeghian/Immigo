from rest_framework.routers import DefaultRouter
from .views import NewsViewset


router = DefaultRouter()

router.register('', NewsViewset, basename='news')

urlpatterns = [
]

urlpatterns += router.urls
