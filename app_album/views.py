# from django.shortcuts import render
from django.views import generic

# スタート
class IndexView(generic.TemplateView):
    template_name = "login.html"

# 新規登録
class Registration_selectView(generic.TemplateView):
    template_name = "registration_select.html"
    
class Teacher_registrationView(generic.TemplateView):
    template_name = "teacher_registration.html"
    
class Student_registrationView(generic.TemplateView):
    template_name = "student_registration.html"
    
class Mail_sendView(generic.TemplateView):
    template_name = "mail_send.html"

# 作成
class Create_menuView(generic.TemplateView):
    template_name = "create_menu.html"

class Teacher_informationView(generic.TemplateView):
    template_name = "teacher_information.html"

class Class_informationView(generic.TemplateView):
    template_name = "class_information.html"

class Event_additionView(generic.TemplateView):
    template_name = "event_addition.html"

class Video_additionView(generic.TemplateView):
    template_name = "video_addition.html"

class Year_inputView(generic.TemplateView):
    template_name = "year_input.html"

# 利用
class TopView(generic.TemplateView):
    template_name = "top.html"

class ProfileView(generic.TemplateView):
    template_name = "profile.html"

class ViewView(generic.TemplateView):
    template_name = "view.html"

class NoticeView(generic.TemplateView):
    template_name = "notice.html"

class Password_ResetView(generic.TemplateView):
    template_name = "password_reset.html"
    
class Password_changeView(generic.TemplateView):
    template_name = "password_change.html"

class LogoutView(generic.TemplateView):
    template_name = "logout.html"
