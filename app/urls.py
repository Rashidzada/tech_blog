from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact,name='contact'),
    path('feedback/',views.feedback,name='feedback'),
    path('display_feed_back/',views.display_feed_back,name='display_feed_back'),
    path('add_news/',views.add_news,name='add_news'),
    path('news_list/',views.news_list,name='news_list'),
    path('news_detail/<int:news_id>/',views.news_detail,name='news_detail')
]