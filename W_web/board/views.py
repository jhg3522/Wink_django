from django.shortcuts import render


# Create your views here.

#메인페이지
def main_index(request):
    return render(request,'index.html')

def post_list(request):
    return render(request,'post_list.html')

