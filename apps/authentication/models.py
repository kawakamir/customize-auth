from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
)
from django.db import models
from django.utils import timezone


# Create your models here.


class StaffManager(BaseUserManager):
    def create_user(self, username, last_name, first_name, password=None):
        if not username:
            raise ValueError("usernameは必須です。")
        if not last_name or not first_name:
            raise ValueError("名前の記入は必須です。")

        staff = self.model(
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

        staff.set_password(password)
        staff.save(using=self._db)
        return staff

    def create_superuser(self, username, last_name, first_name, password):
        staff = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        staff.is_admin = True
        staff.save(using=self._db)
        return staff


class Staff(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField("username", unique=True, max_length=24, db_index=True)
    last_name = models.CharField("名前　姓（カナ）", max_length=24, db_index=True)
    first_name = models.CharField("名前　名（カナ）", max_length=24, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField("作成日時", default=timezone.now)
    updated_at = models.DateTimeField("更新日時", auto_now=True)


class Crew(Staff):
    is_admin = models.BooleanField(default=False)

    object = StaffManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["last_name", "first_name"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class SuperVisor(Staff):
    is_admin = models.BooleanField(default=True)

    object = StaffManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["last_name", "first_name"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
