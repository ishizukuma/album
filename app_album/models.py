from django.db import models
from django.contrib.auth.hashers import make_password


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=60, null=False)


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=60, null=False)


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    mail_address = models.CharField(max_length=100, null=False)
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, null=False)
    number = models.IntegerField(null=False)
    class_name = models.CharField(max_length=20, null=False)
    comment = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=128, null=False)

    def save(self, *args, **kwargs):
        # パスワードをハッシュ化して保存
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    mail_address = models.CharField(max_length=100, null=False)
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50, null=False)
    comment = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=128, null=False)

    def save(self, *args, **kwargs):
        # パスワードをハッシュ化して保存
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
