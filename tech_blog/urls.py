
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static , settings
admin.site.site_title = 'Tech Blog'
admin.site.site_header = 'Tech Blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('',include('accounts.urls')),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
