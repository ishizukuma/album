from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from datetime import datetime

class S3MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

class Photo(models.Model):
    FILE_TYPE_CHOICES = (
        (1, '個人写真'),
        (2, 'アルバム写真'),
        (3, '動画'),
    )

    IMAGE_ID = models.AutoField(primary_key=True)
    IMAGE_NAME = models.CharField(max_length=255, blank=False, null=False)
    FILE_TYPE = models.IntegerField(choices=FILE_TYPE_CHOICES, blank=False, null=False)
    def upload_path(self,filename):
        if self.FILE_TYPE == 2:
            return 'static/images/' + filename
        elif self.FILE_TYPE == 3:
            return 'static/video/' + filename
        else:
            return 'static/other/' + filename

    EVENT_NAME = models.CharField(max_length=50, blank=True, null=True)
    FILE = models.FileField(upload_to=upload_path, storage=S3MediaStorage(), null=True)
    ALBUM_ID = models.IntegerField(blank=True, null=True)
    CLASS_NAME = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'photo'


class S3Model(models.Model):
    FILE_TYPE_CHOICES = (
        (1, '個人写真'),
        (2, 'アルバム写真'),
        (3, '動画'),
    )

    FILE_TYPE = models.IntegerField(choices=FILE_TYPE_CHOICES, blank=False, null=False)
    FILE = models.FileField(upload_to='', storage=S3MediaStorage(), null=True)

    def upload_path(self,filename):
        if self.FILE_TYPE == 2:
            return 'static/images/' + filename
        elif self.FILE_TYPE == 3:
            return 'static/video/' + filename
        else:
            return 'static/other/' + filename

    def save(self, *args, **kwargs):
        self.FILE.upload_to = self.upload_path
        super().save(*args, **kwargs)

class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}: {self.content}"
