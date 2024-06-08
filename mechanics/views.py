from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Mechanics, Reservations
from django.forms.models import model_to_dict

def home(request):
    mechanics_list = Mechanics.objects.all().order_by('-id')

    return render(request, 'mechanics_list.html', {'mechanics_list': mechanics_list})

def reservation(request, mechanic_id):
    mechanic = Mechanics.objects.filter(id=mechanic_id).get()
    
    if request.method == 'POST':
        date = request.POST["date"]
        time = request.POST["time"]
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]

        newMechanic = Reservations(mechanic_id=mechanic, name=name, mobile=mobile,email=email,bookDate=date,bookTime=time)
        newMechanic.save()

        return redirect('thankyou')
    
    return render(request, 'mechanics_book.html', {"mechanic": mechanic})

def checkReservation(request):
    if request.method == 'POST':
        date = request.POST["date"]

        reservation = Reservations.objects.filter(bookDate=date).get()
        
        return JsonResponse({"success": "true", "reservation": model_to_dict(reservation)})

    return JsonResponse({"success": "false"})


def thankyou(request):

    return render(request, 'mechanics_thankyou.html')