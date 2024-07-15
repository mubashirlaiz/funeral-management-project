from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=50)
    current_location = models.CharField(max_length=200)
    funeral_location = models.CharField(max_length=200)
    has_relatives = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name

class FuneralBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='funeral_bookings')
    package_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    

    def __str__(self):
        return f"{self.user.name}'s Booking - {self.package_name}"





class LegalDocument(models.Model):
    DOCUMENT_TYPES = [
        ('Death Certificate', 'Death Certificate'),
        ('Burial Permit', 'Burial Permit'),
        ('Cremation Authorization Form', 'Cremation Authorization Form'),
        # Add other document types as needed
    ]

    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_file = models.FileField(upload_to='legal_documents/')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Legal Document'
        verbose_name_plural = 'Legal Documents'

    def __str__(self):
        return f"{self.document_type} - {self.user.username}"
    

    from django.db import models

class FuneralService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='funeral_service_images/')

    
    def __str__(self):
        return self.name
    


class FuneralPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    


class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.username
    
    
    


class Employee(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Hashed password will be stored here
    role = models.CharField(max_length=100, default='staff')

    def __str__(self):
        return self.username

