# funeral_services/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from funeral_services.models import FuneralBooking,LegalDocument,FuneralService,FuneralPackage,CustomUser,customer,Employee




class FuneralBookingForm(forms.ModelForm):
    class Meta:
        model = FuneralBooking
        fields = ['package_name', 'booking_date',]




class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class LegalDocumentForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['document_type', 'document_file']
        labels = {
            'document_type': 'Document Type',
            'document_file': 'Upload Document File'
        }
        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-select'}),
            'document_file': forms.FileInput(attrs={'class': 'form-control-file'})
        }


class FuneralServiceForm(forms.ModelForm):
    class Meta:
        model = FuneralService
        fields = ['name', 'description', 'image']  

        
class FuneralPackageForm(forms.ModelForm):
    class Meta:
        model = FuneralPackage
        fields = ['name', 'description', 'price']




class user_registrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
    
    


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
    


class EmployeeAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeAuthenticationForm, self).__init__(*args, **kwargs)
        
        # Customize the form fields if needed

    class Meta:
        fields ="__all__"



        
class EmployeeRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'role']