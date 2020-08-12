from django.contrib import admin
from board.models import Board, Document, Comment, Message

admin.site.register(Board)
admin.site.register(Document)
admin.site.register(Comment)
admin.site.register(Message)