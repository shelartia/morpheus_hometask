from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf

# Create your views here.


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '') # Получить из пост запроса юзернейм
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password) # Отправляю логин и пароль в auth
        if user is not None:
            auth.login(request, user) # Авторизация найденного пользователя
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('authuser/login.html', args)
    else:
        return render_to_response('authuser/login.html', args)


def logout(request):
    auth.logout(request) # Делогон пользователя
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm() # Создание элемента словаря и передаеться в него форма из коробки
    if request.POST:
        newuser_form = UserCreationForm(request.POST) # созд новую форму после
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.cleaned_data['username'],
                password=newuser_form.cleaned_data['password2'],)
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('authuser/register.html', args)