
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICE =(
        ('male','남자'),
        ('female','여자'),
    )
    GRADE = ('beginner','god','master')

    name = models.CharField(max_length=20, null=False, verbose_name="이름",)
    userid = models.CharField(max_length=15, null=False, verbose_name="아이디",unique=True)
    password = models.CharField(max_length=15, null=False, verbose_name="비밀번호")
    birth = models.DateField(null=True, verbose_name="생년월일")
    email = models.EmailField(null=False, verbose_name="이메일")
    style = models.CharField(max_length=15,null=True, verbose_name="스타일")
    grade = models.CharField(max_length=10, default="beginner", null=False, verbose_name="등급")
    gender = models.CharField(max_length=20,choices=GENDER_CHOICE, null=True, verbose_name="성별")

