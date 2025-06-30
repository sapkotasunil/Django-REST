from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.studentViews),
    path('students/<int:pk>/',views.studentDetailsView),
    
    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetails.as_view()),  
] 
