from django.shortcuts import render, redirect
from .forms import UploadForm

def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = UploadForm()
    return render(request, "upload.html", {"form": form})
