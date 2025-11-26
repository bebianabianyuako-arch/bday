from django.shortcuts import render

def home(request):
    context = {
        'name': 'Nida Amaliyah',      # Ganti nama dia di sini
        'age': '19th',           # Ganti angka ultah
        'date': '26 November'    # Ganti tanggal
    }
    return render(request, 'wishes/index.html', context)