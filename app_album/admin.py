from django.contrib import admin
from .models import School, Student, Teacher, Album


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["school_id", "school_name"]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ["album_id", "album_name"]


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "school",
        "mail_address",
        "password",
        "student_id",
        "student_name",
        "number",
        "class_name",
        "comment",
    ]


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "school",
        "mail_address",
        "password",
        "teacher_id",
        "teacher_name",
        "comment",
    ]


admin.site.register(School, SchoolAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
