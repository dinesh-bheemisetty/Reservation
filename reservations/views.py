from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm, CancellationForm
from .models import Reservation, Train


# View to handle user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# View to display the homepage
def home(request):
    return render(request, 'home.html')

# View to handle making a reservation
@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_success', pnr_number=reservation.pnr_number)
    else:
         form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})


# View to handle canceling a reservation
# views.py
@login_required
def cancel_reservation(request):
    if request.method == 'POST':
        form = CancellationForm(request.POST)
        if form.is_valid():
            pnr_number = form.cleaned_data['pnr_number']
            try:
                reservation = Reservation.objects.get(pnr_number=pnr_number, user=request.user)
                reservation.delete()
                return redirect('cancellation_success')
            except Reservation.DoesNotExist:
                form.add_error('pnr_number', 'Invalid PNR number')
    else:
        form = CancellationForm()
    return render(request, 'cancellation.html', {'form': form})


# View to show reservation success message
@login_required
def reservation_success(request, pnr_number):
    return render(request, 'reservation_success.html', {'pnr_number': pnr_number})


# View to show cancellation success message
@login_required
def cancellation_success(request):
    return render(request, 'cancellation_success.html')


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html', {'reservations': reservations})