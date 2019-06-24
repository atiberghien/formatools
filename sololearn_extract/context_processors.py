from .forms import SololearnAccountsForm

def sololearn(request):
    return {
        'sololearn_form': SololearnAccountsForm(),
    }