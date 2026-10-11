from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.

def view_page(request):
    return render(request,'crud/home.html')

def employee(request):
   return render(request,'crud/employee.html')


def CreateEmp(request):
    if request.method=='GET':
        return render(request,'crud/createEmp.html')
    elif request.method=='POST':
        emp=Employee()
        emp.image=request.FILES.get('image')  
        emp.name=request.POST.get('name')
        emp.email=request.POST.get('email')
        emp.dob=request.POST.get('dob')
        emp.designation=request.POST.get('designation')
        emp.save()
        return HttpResponse("<h3>employee is added </h3>")
    else:
        return HttpResponse("<p> employee data is not correct </p>")
    

def showData(request):
    if request.method=='GET':
        return render(request, 'crud/employee.html')
    elif request.method=='POST':    
            employees=Employee.objects.all()
            # print(employees)
            context={'emp':employees}
            return render(request, 'crud/employee.html', context=context)
        


def updateEmp(request, id):
    # emp = get_object_or_404(Employee, id=id)  # This fetches a single Employee object
    emp=Employee.objects.get(id=id) #second way
    if request.method == 'POST':
        # Handling the POST request for updating the employee
        emp.image = request.FILES['image']
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.dob = request.POST['dob']
        emp.designation = request.POST['designation']
        emp.save()  # Save the updated employee data to the database
        return redirect('showdata')  # Redirect to the page that shows all employees

    # When it's a GET request, render the form with existing employee data
    return render(request, 'crud/update.html', {'emp': emp})

def  deleteEmp(request,id):
    if request.method=="POST":
        emp=Employee.objects.filter(id=id)
        emp.delete()
        return redirect('showdata')