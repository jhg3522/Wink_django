from django.db import models
from django import forms
# Create your models here.

class User(models.Model):
    #PK, unique, AI 자동생성
    user_name = models.CharField(max_length=20, null=False, verbose_name="이름")
    user_id = models.CharField(max_length=15, null=False, verbose_name="아이디")
    user_password = models.CharField(max_length=15, null=False, verbose_name="비밀번호")
    user_birth = models.DateField(null=False, verbose_name="생년월일")
    user_email = models.EmailField(null=False, verbose_name="이메일")
    user_style = models.CharField(max_length=15, verbose_name="회비 납부 여부")
    user_thumbnail = models.FilePathField(null=True, verbose_name="프로필 사진")
    user_grade = models.CharField(max_length=10, default="beginner",  null=False, verbose_name="등급")
    user_gender = models.CharField(max_length=20, null=False, verbose_name="성별")
