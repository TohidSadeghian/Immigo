from mongoengine import Document, fields
from django.utils.timezone import now



class ErrorDocument(Document):
    error_detail = fields.StringField()
    created_at = fields.DateTimeField(default=now)