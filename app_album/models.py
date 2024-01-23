from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class S3MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

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
    IMAGE_FILE = models.ImageField(upload_to='static/images/', storage=S3MediaStorage(), null=True)
    ALBUM_ID = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'photo'

class S3Model(models.Model):
    IMAGE_FILE = models.ImageField(upload_to='static/images/', storage=S3MediaStorage(), null=True)

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
