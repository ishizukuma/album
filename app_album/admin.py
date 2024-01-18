from django.contrib import admin
from .models import School, Student, Teacher, Album, Profile_student, Profile_teacher


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["school_id", "school_name"]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ["album_id", "album_name"]


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "mail_address",
        "student_id",
        "student_name",
        "password",
    ]


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "mail_address",
        "password",
        "teacher_id",
        "teacher_name",
    ]


class Profile_studentAdmin(admin.ModelAdmin):
    list_display = [
        "profile_student_id",
        "school",
        "album",
        "student",
        "class_name",
        "class_number",
        "comment",
    ]


class Profile_teacherAdmin(admin.ModelAdmin):
    list_display = [
        "profile_teacher_id",
        "school",
        "album",
        "teacher",
        "comment",
    ]


admin.site.register(School, SchoolAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Profile_student, Profile_studentAdmin)
admin.site.register(Profile_teacher, Profile_teacherAdmin)
