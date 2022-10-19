from django.urls import path
from django.contrib import admin

from .views import show_familiar, add_familiar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', show_familiar),
    path('add/<nombre>/<apellido>/<nacimiento>', add_familiar)
]

