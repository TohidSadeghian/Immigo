from mongoengine import Document, fields
from mongoengine.queryset import queryset_manager
from django.utils.timezone import now


class BaseDocument(Document):
    created_at = fields.DateTimeField(default=now)
    updated_at = fields.DateTimeField(null=True)
    is_deleted = fields.BooleanField(default=False)

    meta = {
        'abstract': True
    }

    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.filter(is_deleted=False)