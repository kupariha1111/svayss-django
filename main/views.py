from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def contact(request):
    return render(request, 'main/contact.html')

import csv
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        with open('students.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, email, phone, address])

        return render(request, 'main/register.html', {'success': True})

    return render(request, 'main/register.html')
