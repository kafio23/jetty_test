from django.shortcuts import render
from .forms import LoginForm


def login(request):
    context = {}

    if request.method == 'GET':
        form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    context['form'] = form
    return render(request, "main/login.html", context)
