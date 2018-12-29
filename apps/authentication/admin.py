from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.authentication.models import SuperVisor


# Register your models here.
class SuperVisorCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="パスワード", widget=forms.PasswordInput)
    password2 = forms.CharField(label="パスワード(確認)", widget=forms.PasswordInput)

    class Meta:
        model = SuperVisor
        fields = ("username", "last_name", "first_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("パスワードがあっていません")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SuperVisorChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SuperVisor
        fields = ("username", "last_name", "first_name", "password", "is_active", "is_admin")

    def clean_password(self):
        return self.initial["password"]


class SuperVisorAdmin(BaseUserAdmin):
    form = SuperVisorChangeForm
    add_form = SuperVisorCreationForm

    list_display = ("username", "last_name", "first_name", "is_admin")
    list_filter = ("is_admin",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("last_name", "first_name",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "last_name", "first_name", "password1", "password2")
        }
         ),
    )
    search_fields = ("username",)
    ordering = ("last_name",)
    filter_horizontal = ()


admin.site.register(SuperVisor, SuperVisorAdmin)
admin.site.unregister(Group)
