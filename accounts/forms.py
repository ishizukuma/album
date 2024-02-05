from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "user_type"
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # ユーザータイプ "admin"（0）を選択肢から削除
        self.fields['user_type'].choices = [(key, value) for key, value in self.fields['user_type'].choices if key != 0]

# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "email",
        )