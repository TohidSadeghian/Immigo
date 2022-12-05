import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class BaseModel(models.Model):
    """
    Base model for inheritence for another models.
    """
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    is_deleted = models.BooleanField(_("is_deleted"), default=False)
    # objects = models.Manager() => The default manager.
    objects = BaseManager()

    class Meta:
        abstract = True

class BaseCottage(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE)
    year = models.IntegerField(_("year"))
    customs = models.CharField(_("customs"), max_length=50)
    currency = models.CharField(_("cuurency"), max_length=50)
    assessment_date = models.DateTimeField(_("assessment_date"))
    return_deadline = models.IntegerField(_("return_deadline"))
    maturity_date = models.DateField(_("maturity_date"), auto_now=False, auto_now_add=False)
    currency_rate_type = models.CharField(_("currency_rate_type"), max_length=50)
    remaining = models.DecimalField(_("remaining"), max_digits=8, decimal_places=4)
    operation = models.CharField(_("operation"), max_length=50)

    class Meta:
        abstract = True 
