from django.db import models
from django.contrib.auth.hashers import make_password


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=60, null=False)


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=60, null=False)


class Student(models.Model):
    mail_address = models.CharField(max_length=100, null=False)
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=128, null=False)

    def save(self, *args, **kwargs):
        # パスワードをハッシュ化して保存
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Teacher(models.Model):
    mail_address = models.CharField(max_length=100, null=False)
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=128, null=False)

    def save(self, *args, **kwargs):
        # パスワードをハッシュ化して保存
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Profile_student(models.Model):
    profile_student_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=20, null=False)
    class_number = models.IntegerField(null=False)
    comment = models.CharField(max_length=100, null=False)


class Profile_teacher(models.Model):
    profile_teacher_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, null=False)
