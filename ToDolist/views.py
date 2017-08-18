from django.shortcuts import render, render_to_response

# Create your views here.


def start(request):
    return render_to_response('todolist/main.html')


