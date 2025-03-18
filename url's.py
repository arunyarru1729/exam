from django.urls import path
from systeminfo.views import htop

urlpatterns = [
    path('htop/', htop),
]
