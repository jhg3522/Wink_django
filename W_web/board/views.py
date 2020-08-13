from django.shortcuts import render
from .models import Board

# Create your views here.

#메인페이지
def main_index(request):
    boards = Board.objects
    return render(request,'index.html',{'boards': boards})

def post_list(request):
    boards = Board.objects
    return render(request,'post_list.html',{'boards',boards})

def generic(request):
    boards = Board.objects
    return render(request,'board.html',{'boards': boards})

def board(request):
    boards = Board.objects
    return render(request,'board.html',{'boards': boards})

