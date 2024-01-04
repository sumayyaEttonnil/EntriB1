from datetime import datetime

from django.shortcuts import render
from app1.models import Bus, BoardingStop, DestinationStop, CustomUser, BookedSeat, Stop
from app1.forms import BusForm, BoardingStopForm, DestinationStopForm
from django.forms import inlineformset_factory




def user_list(request):
    users=CustomUser.objects.all()
    return render(request,'user_list.html',{'users':users})


def custom_admin_dashboard(request):
    buses = Bus.objects.all()
    bus_data = []
    print(buses)

    for bus in buses:
        boarding_stops = BoardingStop.objects.filter(bus=bus)
        destination_stops = DestinationStop.objects.filter(bus=bus)

        bus_data.append({
            'bus': bus,
            'boarding_stops': boarding_stops,
            'destination_stops': destination_stops
        })

    return render(request, 'custom_admin_dashboard.html', {'bus_data': bus_data})


from django.shortcuts import get_object_or_404, redirect
from app1.models import Bus

def delete_bus(request, bus_id):
    # Fetch the bus instance based on the provided ID
    bus = get_object_or_404(Bus, id=bus_id)

    if request.method == 'POST':
        # If the request method is POST, delete the bus
        bus.delete()
        # Redirect to a success URL or another page after deletion


    # Handle other HTTP methods if needed
    # ...

    # If not a POST request, render a confirmation page or handle accordingly
    return redirect ('custom_admin_dashboard')


def add_bus(request):
    if request.method == 'POST':
        bus_form = BusForm(request.POST)
        BoardingStopFormSet = inlineformset_factory(Bus, BoardingStop, form=BoardingStopForm, extra=3)
        DestinationStopFormSet = inlineformset_factory(Bus, DestinationStop, form=DestinationStopForm, extra=3)

        if bus_form.is_valid():
            new_bus = bus_form.save(commit=False)
            new_bus.save()

            boarding_stop_formset = BoardingStopFormSet(request.POST, instance=new_bus)
            destination_stop_formset = DestinationStopFormSet(request.POST, instance=new_bus)

            if boarding_stop_formset.is_valid() and destination_stop_formset.is_valid():
                boarding_stop_formset.save()
                destination_stop_formset.save()

                return redirect('custom_admin_dashboard')  # Redirect to a success page

    else:
        bus_form = BusForm()
        BoardingStopFormSet = inlineformset_factory(Bus, BoardingStop, form=BoardingStopForm, extra=3)
        DestinationStopFormSet = inlineformset_factory(Bus, DestinationStop, form=DestinationStopForm, extra=3)
        boarding_stop_formset = BoardingStopFormSet()
        destination_stop_formset = DestinationStopFormSet()

    return render(request, 'add_bus.html', {
        'bus_form': bus_form,
        'boarding_stop_formset': boarding_stop_formset,
        'destination_stop_formset': destination_stop_formset,
    })
from .forms import BusForm1, BoardingStopFormSet, DestinationStopFormSet, BusDateForm, StopForm


def edit_bus(request,bus_id):
    bus = get_object_or_404(Bus, id=bus_id)

    if request.method == 'POST':
        form = BusForm1(request.POST, instance=bus)
        boarding_stop_formset = BoardingStopFormSet(request.POST, instance=bus)
        destination_stop_formset = DestinationStopFormSet(request.POST, instance=bus)

        if form.is_valid() and boarding_stop_formset.is_valid() and destination_stop_formset.is_valid():
            form.save()
            boarding_stop_formset.save()
            destination_stop_formset.save()
            return redirect('custom_admin_dashboard')  # Redirect after successful edit
    else:
        form = BusForm1(instance=bus)
        boarding_stop_formset = BoardingStopFormSet(instance=bus)
        destination_stop_formset = DestinationStopFormSet(instance=bus)

    return render(request, 'edit_bus.html', {
        'form': form,
        'boarding_stop_formset': boarding_stop_formset,
        'destination_stop_formset': destination_stop_formset,
        'bus_id': bus_id
    })

def admin_home(request):
    return render(request,'base_admin.html')



def passenger_details(request):
   if request.method =='POST':
       form=BusDateForm(request.POST)
       if form.is_valid():
           bus_name=form.cleaned_data['bus_name']
           input_date=form.cleaned_data['date']
           date = input_date.strftime('%Y-%m-%d')
           print(bus_name)

           booked_seats=BookedSeat.objects.filter(bus_name=bus_name,date=date)
           context={'booked_seats': booked_seats,
                  'bus_name': bus_name,
                   'date': date
                    }
           return render(request,'passenger_details_page.html',context)
   else:
       form=BusDateForm()
   return render(request,'busdate.html',{'form':form})



def add_stop(request):
    if request.method=='POST':
        stop_form=StopForm(request.POST)
        if stop_form.is_valid():
            new_stop=stop_form.save(commit=False)
            new_stop.save()
            return redirect('stop_list')
    else:
        stop_form=StopForm()

    return render(request,'add_stop.html',{'stop_form':stop_form})


def stop_list(request):
    stops=Stop.objects.all()
    return render(request,'stop_list.html',{'stops':stops})



def delete_stop(request,stop_id):
    stop=get_object_or_404(Stop,id=stop_id)
    if request.method == 'POST':
        stop.delete()
    return redirect('stop_list')
