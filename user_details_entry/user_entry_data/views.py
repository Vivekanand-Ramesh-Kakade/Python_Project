from django.shortcuts import render
from django.http import JsonResponse
import openpyxl
import os

def home(request):
    return render(request, "User_entry_form.html")

def submit(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        age = request.POST.get("age")
        nationality = request.POST.get("nationality")

        file_path = os.path.join(os.path.dirname(__file__), "user_data.xlsx")


        # Create file if not exists
        if not os.path.exists(file_path):
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(["Username", "First Name", "Last Name", "Email", "DOB", "Age", "Nationality"])
            print("Saving data:", username, first_name, last_name, email, dob, age, nationality)
            wb.save(file_path)

        # Append data
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        ws.append([username, first_name, last_name, email, dob, age, nationality])
        print("Saving data:", username, first_name, last_name, email, dob, age, nationality)
        wb.save(file_path)

        return JsonResponse({"status": "success"})
