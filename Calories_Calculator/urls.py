from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logoutUser'),
    path('signup/',views.signup, name='signup'),
    path('user_details/',views.user_details, name='add_details'),
    path('add_food/',views.add_food, name='add_food')
]