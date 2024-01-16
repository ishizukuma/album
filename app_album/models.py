from django.db import models

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

    class Meta:
        db_table = 'photo'  # テーブル名を適切に設定してください
