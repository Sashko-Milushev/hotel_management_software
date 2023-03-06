from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    pass
