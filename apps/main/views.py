from django.shortcuts import render, redirect
from .forms import LoginForm
from ..drivers.models import Driver
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

            try:
                response = req.post(
                    'https://jettymx-st.herokuapp.com/api/drivers/session', json=payload)

                response_parameters = response.json()
                print(response_parameters)

                if "id" in response_parameters:
                    context['show_alert'] = False
                    context['email'] = response_parameters['email']
                    context['auth_token'] = response_parameters['auth_token']
                    context['driver_id'] = response_parameters['id']

                    driver, created = Driver.objects.get_or_create(
                        email=response_parameters['email'], defaults={
                            'auth_token': response_parameters['auth_token'],
                            'driver_id': response_parameters['id']}
                    )

                    if created:
                        driver = Driver(
                            driver_id=response_parameters['id'], email=response_parameters['email'], auth_token=response_parameters['auth_token'])
                        driver.save()

                    else:
                        # driver exists
                        driver.driver_id = response_parameters['id']
                        driver.auth_token = response_parameters['auth_token']
                        driver.save()

                    return redirect('drivers_url', driver_id=driver.driver_id)

                if "code" in response_parameters:
                    context['show_alert'] = True
                    context['message'] = response_parameters['message']

            except Exception as e:
                print(e)

    context['form'] = form
    return render(request, "main/login.html", context)
