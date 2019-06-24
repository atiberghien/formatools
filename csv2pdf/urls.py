from django.urls import path
from .views import CSV2PDFFormView

urlpatterns = [
    path('', CSV2PDFFormView.as_view(), name="csv2pdf"),
]
