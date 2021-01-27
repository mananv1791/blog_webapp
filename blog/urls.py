from django.contrib import admin
from django.urls import path,include
from app1 import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls'))
]
