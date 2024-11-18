from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact,name='contact'),
    path('feedback/',views.feedback,name='feedback'),
    path('display_feed_back/',views.display_feed_back,name='display_feed_back')
]