from django import forms


class SololearnAccountsForm(forms.Form):
    account_list = forms.CharField(widget=forms.Textarea, required=True)