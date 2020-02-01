from django.shortcuts import render
from .forms import LoginForm
import requests as req


def login(request):
    context = {}
    context['show_alert'] = False

    if request.method == 'GET':
        form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            parameters = form.cleaned_data
            payload = {"driver": parameters}
            print(payload)
            try:
                response = req.post(
                    'https://jettymx-st.herokuapp.com/api/drivers/session', json=payload)

                response_parameters = response.json()
                if "code" in response.json():
                    context['show_alert'] = True
                    context['message'] = response_parameters['message']
                print(response_parameters)

            except Exception as e:
                print(e)

    context['form'] = form
    return render(request, "main/login.html", context)
