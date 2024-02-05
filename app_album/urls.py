from django.urls import path

from . import views

app_name = 'app_album'
urlpatterns = [
    path('', views.IndexView.as_view(), name="top"),
    
    # 新規登録
    path('mail_send/', views.Mail_sendView.as_view(), name="mail_send"),
    
    # 作成
    path('create_menu/', views.Create_menuView.as_view(), name="create_menu"),
    path('teacher_information/', views.Teacher_informationView.as_view(), name="teacher_information"),
    path('class_information/', views.Class_informationView.as_view(), name="class_information"),
    path('event_addition/', views.Event_additionView.as_view(), name="event_addition"),
    path('video_addition/', views.Video_additionView.as_view(), name="video_addition"),
    path('year_input/', views.Year_inputView.as_view(), name="year_input"),
    
    # 利用
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('view/', views.ViewView.as_view(), name="view"),
    path('notice/', views.NoticeView.as_view(), name="notice"),
    path('password_reset/', views.Password_ResetView.as_view(), name="password_reset"),
    path('password_change/', views.Password_changeView.as_view(), name="password_change"),
]
