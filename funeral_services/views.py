

# Create your views here.

from funeral_services.models import User,FuneralBooking,LegalDocument,FuneralService,FuneralPackage,customer
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from funeral_services.forms import FuneralBookingForm,UserLoginForm,LegalDocumentForm,FuneralServiceForm,FuneralPackageForm,user_registrationForm,UserRegistrationForm,EmployeeAuthenticationForm,EmployeeRegistrationForm
import os
from django.views import View
from django.contrib.auth.decorators import login_required




class user_registration(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,"user_registration.html",{"data":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            customer.objects.create(**form.cleaned_data)
        return render(request,"home.html")





def book_funeral(request):
    if request.method == 'POST':
        form = FuneralBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')  # Redirect to a success page or dashboard
    else:
        form = FuneralBookingForm()

    return render(request, 'book_funeral.html', {'form': form})





def home(request):
    return render(request, 'home.html')



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Login the user
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('book_funeral')  # Redirect to the dashboard after successful login
            else:
                messages.error(request, 'Invalid username or password.')

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})





def base_view(request):
    return render(request, 'base.html')



def user_logout(request):
    logout(request)
    return redirect('home')  




def create_legal_document(request):
    if request.method == 'POST':
        form = LegalDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')  # Redirect to document list page after successful submission
    else:
        form = LegalDocumentForm()
    return render(request, 'create_legal_document.html', {'form': form})


def document_list(request):
    documents = LegalDocument.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def download_document(request, document_id):
    document = get_object_or_404(LegalDocument, pk=document_id)
    file_path = document.document_file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')  # Adjust content type as needed
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    return HttpResponse('File not found', status=404)


def delete_document(request, document_id):
    document = get_object_or_404(LegalDocument, pk=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')  # Redirect to document list page after successful deletion
    return render(request, 'confirm_delete_document.html', {'document': document})


def funeral_services(request):
    services = FuneralService.objects.all()
    return render(request, 'services.html', {'services': services})

def create_funeral_service(request):
    if request.method == 'POST':
        form = FuneralServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('funeral_services')
    else:
        form = FuneralServiceForm()
    return render(request, 'services.html', {'form': form})



def funeral_package_list(request):
    packages = FuneralPackage.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

def create_funeral_package(request):
    if request.method == 'POST':
        form = FuneralPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')  # Redirect to package list page after creating a package
    else:
        form = FuneralPackageForm()
    return render(request, 'create_package.html', {'form': form})


# views.py


def register(request):
    if request.method == 'POST':
        form = user_registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Redirect to home page or any other page
    else:
        form = user_registrationForm()
    return render(request, 'registration.html', {'form': form})


class PakageView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=FuneralPackage.objects.get(id=id)
        return render(request,"pakageview.html",{"data":data})
    

def logout_view(request):
    logout(request)
    return redirect('home')



class EmployeeLoginView(View):
    def get(self, request):
        form = EmployeeAuthenticationForm()
        return render(request, 'dashboard', {'form': form})

    def post(self, request):
        form = EmployeeAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect authenticated employees to a specific page
                return redirect('dashboard')  # Replace 'dashboard' with the URL name of the employee dashboard
        # If authentication fails or form is invalid, render the login page again with error message
        return render(request, 'dashboard', {'form': form, 'error_message': 'Invalid credentials'})
    



def employee_dashboard(request):
    # Logic to retrieve data or perform operations for the dashboard
    # For example, you can fetch information related to funeral services, customer requests, etc.
    
    # Render the employee dashboard HTML template
    return render(request, 'dashboard')





def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            # Save the employee to the database
            form.save()
            return redirect('employee_login.html')  # Redirect to login page after successful registration
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'employee_login.html', {'form': form})