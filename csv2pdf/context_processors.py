from .forms import CSV2PDFForm

def csv2pdf(request):
    return {
        'csv2pdf_form': CSV2PDFForm(),
    }