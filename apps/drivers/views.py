from django.shortcuts import render, redirect
from .models import Driver
import requests as req


def driver(request, driver_id):
    context = {}
    context['trips'] = []

    driver = Driver.objects.get(driver_id=driver_id)

    authorization = 'Token {},email={}'.format(
        driver.auth_token, driver.email)
    headers = {'Content-Type': 'application/json',
               'Authorization': authorization}
    try:
        response = req.get(
            'https://jettymx-st.herokuapp.com/api/drivers/trips', headers=headers)

        if response.status_code == 200:
            trips = response.json()
            context['trips'] = trips
        else:
            return redirect('login_url')
    except:
        return redirect('login_url')

    return render(request, "drivers/trips_list.html", context)
