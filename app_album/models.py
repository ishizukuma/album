from django.db import models
from datetime import datetime

# Create your models here.
class Photo(models.Model):
    IMAGE_TYPE_CHOICES = (
        (1, '個人写真'),
        (2, 'アルバム写真'),
        (3, '動画'),
    )

    IMAGE_ID = models.AutoField(primary_key=True)
    IMAGE_NAME = models.CharField(max_length=255, blank=False, null=False)
    IMAGE_TYPE = models.IntegerField(choices=IMAGE_TYPE_CHOICES, blank=False, null=False)
    EVENT_NAME = models.CharField(max_length=50, blank=True, null=True)
    ALBUM_ID = models.IntegerField(blank=True, null=True)
    CLASS_NAME = models.CharField(max_length=20, blank=True, null=True)  # 追加

    class Meta:
        db_table = 'photo'


class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.content
