from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

#for using viewset
router=DefaultRouter()
#creating standard REST API routes (like list, retrieve, create, update, delete) for EmployeeViewSet, and prefix all routes with /employees/.”
router.register('employees',views.EmployeeViewSet,basename='employee') #DRF needs a base name to generate names for the URL patterns (like employee-list, employee-detail).


urlpatterns = [
    path('students/',views.studentViews),
    path('students/<int:pk>/',views.studentDetailsView),
    
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetails.as_view()), 
    
     #for using viewset
     
     path('',include(router.urls)),
     path('blogs/',views.BlogsView.as_view()),
     path('comments/',views.CommentsView.as_view()),
] 
