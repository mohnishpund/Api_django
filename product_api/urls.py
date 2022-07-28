from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('peoples/', include('django.contrib.auth.urls')),
    path('peoples/', include('peoples.urls')),

]
