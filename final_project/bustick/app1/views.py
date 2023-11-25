from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


from .forms import UserRegistration, BusStopSelectionForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})


def signout(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        request.session['last_logged_out'] = username
        last_logged_out_user = request.session.get('last_logged_out')
    return render(request, 'logout.html', {'last_logged_out_user': last_logged_out_user})


from .models import Bus, BoardingStop, DestinationStop, BookedSeat


def search_buses(request):
    if request.method == 'POST':
        source_stop_name = request.POST.get('source')
        dest_stop_name = request.POST.get('destination')
        date = request.POST.get('date')
        formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')

        source_stop_name_upper = source_stop_name.upper()
        dest_stop_name_upper = dest_stop_name.upper()
        buses_with_source = Bus.objects.filter(boarding_stops__name=source_stop_name_upper)
        buses_with_destination = Bus.objects.filter(destination_stops__name=dest_stop_name_upper)
        common_buses = buses_with_source.intersection(buses_with_destination)
        buses_info = []
        min_p = 10
        for bus in common_buses:
            boarding_info = BoardingStop.objects.filter(bus=bus, stop__name=source_stop_name_upper).first()
            destination_info = DestinationStop.objects.filter(bus=bus, stop__name=dest_stop_name_upper).first()
            if boarding_info and destination_info:
                boarding_datetime = datetime.combine(datetime.today(), boarding_info.departure_time)
                destination_datetime = datetime.combine(datetime.today(), destination_info.arrival_time)
                print(destination_datetime)
                print(boarding_datetime)
                duration = destination_datetime - boarding_datetime
                str1 = str(duration).split(',')
                if len(str1) > 1:
                    str2 = str1[1].split(':')
                    duration1 = str2[0] + 'hours' + str2[1] + 'minutes'
                else:
                    str2 = str1[0].split(':')
                    duration1 = str2[0] + 'hours' + str2[1] + 'minutes'

                distance = destination_info.distance - boarding_info.distance
                price = min_p * distance
                buses_info.append({
                    'bus': bus,
                    'departure_time': boarding_info.departure_time,
                    'arrival_time': destination_info.arrival_time,
                    'duration1': duration1,
                    'price': price,
                    'total_seats': bus.total_seats,  # Include total seats
                    'bus_type': bus.get_bus_type_display()
                })

            # print(bus.get_bus_type_display)
        context = {
            'buses_info': buses_info,
            'source_stop_name': source_stop_name_upper,
            'dest_stop_name': dest_stop_name_upper,
            'date': formatted_date,
            'num': list(range(1, 13))
        }

        return render(request, 'available_buses.html', context)
    else:
        form = BusStopSelectionForm()

    return render(request, 'search.html', {'form': form})


def seat(request):
    row_number = {'num': list(range(1, 13))}

    return render(request, 'seat1.html', row_number)


from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def your_backend_booking_endpoint(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bus_id = data.get('busId')
            input_date = data.get('date')
            date_object = datetime.strptime(input_date, '%d-%m-%Y')
            date = date_object.strftime('%Y-%m-%d')
            passenger_details = data.get('passengerDetails')

            booked_seats = []

            for seat in passenger_details:
                seat_number = seat['seatNumber'].strip()

                # Check if the seat is already booked for the same bus and date
                seat_exists = BookedSeat.objects.filter(bus_id=bus_id, date=date, seat_number=seat_number).exists()

                if not seat_exists:
                    # Seat is not booked, save it to the database
                    passenger_name = seat['passengerName']
                    passenger_gender = seat['passengerGender']
                    booked_seat = BookedSeat(
                        bus_id=bus_id,
                        date=date,
                        seat_number=seat_number,
                        passenger_name=passenger_name,
                        passenger_gender=passenger_gender,
                        status='Booked'
                    )
                    booked_seat.save()

                    # Append the booked seat details to the list
                    booked_seats.append(seat)
                else:
                    # Seat is already booked for the same bus and date
                    # Add it to the list of already booked seats
                    booked_seats.append({
                        'seatNumber': seat_number,
                        'alreadyBooked': True
                    })

            return JsonResponse({
                "message": "Seats booked successfully",
                "data": {
                    "busId": bus_id,
                    "date": date,
                    "bookedSeats": passenger_details,
                    "alreadyBookedSeats": booked_seats
                }
            }, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def payment_view(request):
    total_price = request.GET.get('totalPrice')
    return render(request, 'payment.html', {'total_price': total_price})
