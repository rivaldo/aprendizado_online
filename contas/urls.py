from django.urls import path
from contas.views import index

urlpatterns = [
    path('', index)
]
