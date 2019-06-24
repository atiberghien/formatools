from django import forms


class CSV2PDFForm(forms.Form):
    page_label = forms.CharField(initial="Page", required=True)
    csv_file = forms.FileField(required=True)