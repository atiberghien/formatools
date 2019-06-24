from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('tool/csv2pdf', include('csv2pdf.urls')),
    path('tool/sololearn', include('sololearn_extract.urls')),
]
