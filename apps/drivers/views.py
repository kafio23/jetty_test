from django.shortcuts import render, redirect
from .models import Driver
import requests as req
from operator import itemgetter
import itertools


def driver(request, driver_id):
    context = {}
    context['trips'] = []
    context['new_trips_list'] = []

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
            new_trips_list = []
            trip_list = []

            trip_group_by_date = sorted(trips, key=itemgetter('date'))
            for key, value in itertools.groupby(trip_group_by_date, key=itemgetter('date')):
                for element in value:
                    trip_list.append(element)

            context['trips'] = trip_list

            for trip in trip_list:
                trip['first_trip_stop'] = trip['trip_stops'][0]
                trip['last_trip_stop'] = trip['trip_stops'][-1]
                trip['filtered_trip_stops'] = []
                if len(trip['trip_stops']) > 2:
                    trip['filtered_trip_stops'] = trip['trip_stops'][1:-1]

            trip_group_by_date = sorted(trip_list, key=itemgetter('date'))
            for key, value in itertools.groupby(trip_group_by_date, key=itemgetter('date')):
                new_trips_list.append({key: value})

            context['new_trips_list'] = new_trips_list
        else:
            return redirect('login_url')
    except Exception as e:
        print(e)
        return redirect('login_url')

    return render(request, "drivers/trips_list.html", context)
