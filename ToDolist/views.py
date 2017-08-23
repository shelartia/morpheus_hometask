from django.shortcuts import render, render_to_response
# Create your views here.


def start(request):
    context = {
        'title': 'TODO List title',

    }
    return render_to_response('todolist/base.html', context)


