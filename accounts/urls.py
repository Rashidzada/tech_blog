from django.urls import path
from .import views
urlpatterns = [
    path('login_view/',views.login_view,name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('dashbaord/',views.dashbaord,name='dashbaord'),
    
    path('signup/',views.signup,name='signup'),
]