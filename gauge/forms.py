from django import forms

class BMIForm(forms.Form):
    weight = forms.FloatField(label='Weight (kg)', min_value=20, max_value=300, widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
            }
        )
        )
    height = forms.FloatField(label='Height (cm)', min_value=50, max_value=250, widget=forms.NumberInput(
        attrs={'class': 'form-control'}
        )
    )

