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

class Event_additionView(View):
    template_name = "event_addition.html"

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
                IMAGE_TYPE=2,  # 2に固定
                EVENT_NAME=event_tag,
                IMAGE_FILE=image,
            )

        # フォームの処理が成功した場合、適切なページにリダイレクト
        request.session['success_messages'] = ['アップロードが成功しました。']
        return redirect('app_album:event_addition')

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

class NoticeView(View):
    template_name = "notice.html"

    def get(self, request, *args, **kwargs):
        # データベースからメッセージを取得
        messages = Message.objects.all()
        form = MessageForm()
        return render(request, self.template_name, {'messages': messages, 'form': form})

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)

        if form.is_valid():
            # メッセージをデータベースに保存
            Message.objects.create(content=form.cleaned_data['message'])

        # データベースから更新されたメッセージを取得
        messages = Message.objects.all()
        return render(request, self.template_name, {'messages': messages, 'form': form})



def notice_view(request):
    if request.method == 'GET':
        # データベースからメッセージを取得
        messages = Message.objects.all()
        form = MessageForm()
        return render(request, 'notice.html', {'messages': messages, 'form': form})

    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # メッセージをデータベースに保存
            Message.objects.create(content=form.cleaned_data['message'])

        # データベースから更新されたメッセージを取得
        messages = Message.objects.all()
        return render(request, 'notice.html', {'messages': messages, 'form': form})


class Password_ResetView(generic.TemplateView):
    template_name = "password_reset.html"

class Password_changeView(generic.TemplateView):
    template_name = "password_change.html"

class LogoutView(generic.TemplateView):
    template_name = "logout.html"
