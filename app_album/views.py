# from django.shortcuts import render
from django.views import generic
from django.views import View
from django.shortcuts import render,redirect
from .models import Photo
from .models import Message
from django.http import HttpResponse
from .models import Photo, S3Model
from django.conf import settings
import boto3
from botocore.exceptions import NoCredentialsError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
# スタート
class IndexView(generic.TemplateView,LoginRequiredMixin,View):
    template_name = "top.html"
    login_url = reverse_lazy("accounts:index")

class Mail_sendView(generic.TemplateView,LoginRequiredMixin):
    template_name = "mail_send.html"
    login_url = reverse_lazy("accounts:index")
# 作成
class Create_menuView(generic.TemplateView,LoginRequiredMixin):
    template_name = "create_menu.html"
    login_url = reverse_lazy("accounts:index")

class Teacher_informationView(generic.TemplateView,LoginRequiredMixin):
    template_name = "teacher_information.html"
    login_url = reverse_lazy("accounts:index")

class Class_informationView(generic.TemplateView,LoginRequiredMixin):
    template_name = "class_information.html"
    login_url = reverse_lazy("accounts:index")

class Event_additionView(View,LoginRequiredMixin):
    template_name = "event_addition.html"
    login_url = reverse_lazy("accounts:index")

    def get(self, request, *args, **kwargs):
        # セッションからメッセージを取得
        success_messages = request.session.get('success_messages', None)
        if success_messages:
            # メッセージがある場合は取得後にセッションから削除
            del request.session['success_messages']
        context = {'success_messages': success_messages}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POSTメソッドの処理
        event_tag = request.POST.get('event_tag')
        images = request.FILES.getlist('images[]')

        for image in images:
            # 拡張子を取り除いたファイル名を取得
            image_name = image.name.rsplit('.', 1)[0]
            # モデルを作成
            photo = Photo.objects.create(
                IMAGE_NAME=image_name,
                FILE_TYPE=2,  # 2に固定
                EVENT_NAME=event_tag,
                FILE=image,
            )

        # フォームの処理が成功した場合、適切なページにリダイレクト
        request.session['success_messages'] = ['アップロードが成功しました。']
        return redirect('app_album:event_addition')

class Video_additionView(generic.TemplateView,LoginRequiredMixin):
    template_name = "video_addition.html"
    login_url = reverse_lazy("accounts:index")

    def get(self, request, *args, **kwargs):
        # セッションからメッセージを取得
        success_messages = request.session.get('success_messages', None)
        if success_messages:
            # メッセージがある場合は取得後にセッションから削除
            del request.session['success_messages']
        context = {'success_messages': success_messages}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POSTメソッドの処理
        event_tag = request.POST.get('event_tag')
        videos = request.FILES.getlist('video[]')

        for video in videos:
            # 拡張子を取り除いたファイル名を取得
            video_name = video.name.rsplit('.', 1)[0]
            # モデルを作成
            photo = Photo.objects.create(
                IMAGE_NAME=video_name,
                FILE_TYPE=3,  # 2に固定
                EVENT_NAME=event_tag,
                FILE=video,
            )

        # フォームの処理が成功した場合、適切なページにリダイレクト
        request.session['success_messages'] = ['アップロードが成功しました。']
        return redirect('app_album:video_addition')

class Year_inputView(generic.TemplateView,LoginRequiredMixin):
    template_name = "year_input.html"
    login_url = reverse_lazy("accounts:index")

class ProfileView(generic.TemplateView,LoginRequiredMixin):
    template_name = "profile.html"
    login_url = reverse_lazy("accounts:index")


class ViewView(generic.TemplateView,LoginRequiredMixin):
    template_name = "view.html"
    login_url = reverse_lazy("accounts:index")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 検索クエリがある場合は絞り込み
        search_query = self.request.GET.get('search', '')
        photos = Photo.objects.filter(EVENT_NAME__icontains=search_query)

        # EVENT_NAMEの一覧を取得して重複を排除
        event_names = Photo.objects.values_list('EVENT_NAME', flat=True).distinct()

        # CLASS_NAMEの一覧を取得して重複を排除
        class_names = Photo.objects.values_list('CLASS_NAME', flat=True).distinct()

        # ユーザーが選択したEVENT_NAMEとCLASS_NAMEの値を取得
        selected_event_name = self.request.GET.get('event_search', '')
        selected_class_name = self.request.GET.get('class_search', '')

        # イベント名で絞り込み
        if selected_event_name:
            photos = photos.filter(EVENT_NAME=selected_event_name)

        # クラス名で絞り込み
        if selected_class_name:
            photos = photos.filter(CLASS_NAME=selected_class_name)

        context['photos'] = photos
        context['event_names'] = event_names
        context['class_names'] = class_names
        context['selected_event_name'] = selected_event_name
        context['selected_class_name'] = selected_class_name

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            uploaded_file = request.FILES.get('file')  # フォームで指定したファイルのフィールド名
            if uploaded_file:
                S3Model.objects.create(IMAGE_FILE=uploaded_file)
                return redirect('success_page')
        return render(request, 'view.html')


from .forms import MessageForm

class NoticeView(LoginRequiredMixin, View):
    template_name = "notice.html"
    login_url = reverse_lazy("accounts:index")

    def get(self, request, *args, **kwargs):
        messages = Message.objects.all()
        form = MessageForm()
        return render(request, self.template_name, {'messages': messages, 'form': form})

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(content=form.cleaned_data['content'])
        messages = Message.objects.all()
        return render(request, self.template_name, {'messages': messages, 'form': form})

class Password_ResetView(generic.TemplateView,LoginRequiredMixin):
    template_name = "password_reset.html"
    login_url = reverse_lazy("accounts:index")


class Password_changeView(generic.TemplateView,LoginRequiredMixin):
    template_name = "password_change.html"
    login_url = reverse_lazy("accounts:index")

def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content.strip():  # 空でないメッセージの場合のみ保存
            Message.objects.create(content=content)
    return redirect('app_album:notice')  # チャット画面にリダイレクト
