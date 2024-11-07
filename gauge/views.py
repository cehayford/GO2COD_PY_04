from django.shortcuts import render
from .forms import BMIForm

def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            if bmi < 18.5:
                category = 'Underweight'
            elif 18.5 <= bmi < 25:
                category = 'Normal weight'
            elif 25 <= bmi < 30:
                category = 'Overweight'
            else:
                category = 'Obese'
            return render(request, 'gauge/homepage.html', {'form': form, 'bmi': round(bmi, 2), 'category': category})
    else:
        form = BMIForm()
    return render(request, 'gauge/homepage.html', {'form': form})
