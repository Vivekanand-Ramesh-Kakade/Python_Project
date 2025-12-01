from django.shortcuts import render
from .models import Record

def show_data(request):
    records = Record.objects.all()
    return render(request, 'viewer/table.html', {'records': records})
