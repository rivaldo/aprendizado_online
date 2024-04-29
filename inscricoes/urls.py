from django.urls import path
from inscricoes.views import inscricoes

urlpatterns = [
    path('', inscricoes)
]
