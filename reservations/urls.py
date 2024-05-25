from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('reserve/', views.make_reservation, name='make_reservation'),
    path('cancel/', views.cancel_reservation, name='cancel_reservation'),
    path('home', views.home, name='home'),
    path('reservation_success/<uuid:pnr_number>/', views.reservation_success, name='reservation_success'),
    path('cancellation_success/', views.cancellation_success, name='cancellation_success'),
    path('my_reservations/', views.reservation_list, name='reservation_list'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  

]
