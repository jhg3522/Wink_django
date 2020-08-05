from django.db import models
from django.utils.timezone import now
from account.models import User


# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=15, null=False, verbose_name="게시판 이름")
    write_permission = models.BooleanField(null=False, default=False, verbose_name="쓰기 권한")
    read_permission = models.BooleanField(null=False, default=True, verbose_name="열람 권한")


class Document(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="게시물 제목")
    content = models.TextField(max_length=5000, null=False, verbose_name="게시물 내용")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="게시물 주인")
    m_date = models.DateTimeField(default=now, verbose_name="작성일")
    write_permission = models.BooleanField(null=False, default=False, verbose_name="쓰기 권한")
    attachment_img = models.FilePathField(null=True, verbose_name="첨부 사진")

class Comment(models.Model):
    post_id = models.ForeignKey(Document, on_delete=models.CASCADE, null=False, verbose_name="게시물 대상")
    re_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name="대댓글 대상")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="댓글 소유자")
    m_date = models.DateTimeField(default=now, verbose_name="작성일")
    read_permission = models.BooleanField(null=False, default=True, verbose_name="열람 권한")

class Recommend(models.Model):
    post_id = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, verbose_name="게시물 번호")
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, verbose_name="댓글 번호")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="추천 소유자")
    date = models.DateTimeField(default=now, verbose_name="추천 한 날짜")

class Message(models.Model):
    send_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, verbose_name="보낸 사람" )
    receive_id = models.ForeignKey(User , on_delete=models.SET_NULL, null=True, verbose_name="받는 사람")
    content = models.TextField(max_length=5000, null=False, verbose_name="쪽지 내용")
    date = models.DateTimeField(default=now, verbose_name="보낸 날짜")