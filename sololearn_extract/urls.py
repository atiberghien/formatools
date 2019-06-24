from django.urls import path
from .views import SololearnAccountFormView

urlpatterns = [
    path('', SololearnAccountFormView.as_view(), name="sololearn_extract"),
]
