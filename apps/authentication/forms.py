from django import forms
import zenhan
from apps.authentication.models import Staff
from apps.admin.strings import Strings


class CrewRegisterForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ("username", "last_name", "first_name")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not Strings.is_alphabet(username):
            raise forms.ValidationError("入力できるのはアルファベット、数字、ハイフン、アンダーバー、半角スペースのみです。")
        return username

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not Strings.is_kana(last_name):
            raise forms.ValidationError("入力できるのはカタカナのみです。")
        return zenhan.h2z(last_name)

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not Strings.is_kana(first_name):
            raise forms.ValidationError("入力できるのはカタカナのみです。")
        return zenhan.h2z(first_name)