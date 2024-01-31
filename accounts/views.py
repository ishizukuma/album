from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user_type = form.cleaned_data.get("user_type", None)
        
          # ユーザータイプが "admin" の場合はエラーとする
        if user_type == 0:
            form.add_error("user_type", "Invalid user type.")
            return self.form_invalid(form)
        
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form) 
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, username=username, password=password,user_type=user_type)

        if user and user_type != 0:
            login(self.request, user)
        return response

# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"
    
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")