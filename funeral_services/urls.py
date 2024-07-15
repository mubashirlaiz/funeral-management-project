# funeral_services/urls.py
from django.urls import path
from django.conf import settings
from funeral_services import views
from django.conf.urls.static import static

urlpatterns = [
    path('user_register/', views.user_registration.as_view(), name='user_registration'),
    path('book_funeral/', views.book_funeral, name='book_funeral'),
    path('legal_documentation/', views.create_legal_document, name='legal_documentation'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('base/', views.base_view, name='base_view'),
    path('logout/',views.user_logout, name='user_logout'),
    path('services/',views.funeral_services, name='funeral_services'),
    path('packages/', views.funeral_package_list, name='package_list'),
    path('packages/create/', views.create_funeral_package, name='create_package'),
    path('register/',views.register, name='register'),
    path('pakagedet/<int:pk>',views.PakageView.as_view(),name='pakage_view'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.employee_dashboard, name='dashboard'),
    path('employee/register/',views. employee_registration, name='employee_register'),
    path('employee/employee_login/',views.EmployeeLoginView.as_view(), name='employee_login')

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
