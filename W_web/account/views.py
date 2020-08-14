from django.shortcuts import render,redirect
from django.contrib.auth import models, views, login
from django.views.generic import CreateView
from .form import UserForm
# Create your views here.
def sign(request):
    return render(request,'signup.html')

def logout(request):
    return render(request,'index.html')

class UserCreateView(CreateView):
    form_class = UserForm
    template_name='reviewBoard/signup.html'
    success_url = "/"

def signup(request):
    if request.method == "POST":  # 1
        form = UserForm(request.POST)

        if form.is_valid():  # 2
            new_user = models.User.objects.create_user(**form.cleaned_data)  # 5
            login(request, new_user)

        return redirect('reviewBoard:index')

    else:  # 3
        form = UserForm()

    return render(request, 'reviewBoard/signup.html', {'form': form})  # 4