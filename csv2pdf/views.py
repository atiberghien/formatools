from django.shortcuts import render
from django.views.generic import FormView
from django_weasyprint import WeasyTemplateResponseMixin
from .forms import CSV2PDFForm
from collections import OrderedDict
import csv
import io

class CSV2PDFFormView(WeasyTemplateResponseMixin, FormView):
    form_class = CSV2PDFForm
    http_method_names = ['post', 'head', 'options']
    template_name = "csv2pdf/pdf.html"
    pdf_filename = 'csv2pdf.pdf'

    def get_context_data(self, **kwargs):
        context = FormView.get_context_data(self, **kwargs)
        
        form = context["form"]
        headers = []
        context["contents"] = []
        if form.is_valid():
            f = io.StringIO(form.cleaned_data["csv_file"].read().decode('utf-8'))
            csv_reader = csv.reader(f, delimiter=',')
            headers = next(csv_reader)
            for row in csv_reader:
                content = OrderedDict({})
                for i, header in enumerate(headers):
                    content[header] = row[i]
                context["contents"].append(content)
        return context
        
    def form_valid(self, form):
        return WeasyTemplateResponseMixin.render_to_response(self, self.get_context_data(form=form))

    def form_invalid(self, form):
        return FormView.render_to_response(self, self.get_context_data(form=form))

