from django import forms


class BuySellForm(forms.Form):
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    amount = forms.IntegerField()

class SellForm(forms.Form):
    price = forms.DecimalField(widget=forms.NumberInput)
    amount = forms.IntegerField()