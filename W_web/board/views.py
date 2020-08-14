from django.shortcuts import render, redirect,get_object_or_404
from .models import Board, Document
from django.utils.timezone import now


# Create your views here.

#메인페이지
def main_index(request):
    document = Document()
    return render(request,'index.html',{'document':document})

def post_list(request):

    return render(request,'post_list.html')

def generic(request):
    return render(request,'generic.html')

def board(request):
    return render(request,'board.html')

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html',{'board':board_detail})

def create(request):
    document = Document()
    document.title = request.GET['title']
    document.content = request.GET['content']
    document.m_date = now()
    document.save()
    return redirect('/board/'+str(document.title))

