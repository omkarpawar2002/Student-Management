from django.urls import path
from .views import ( Add_Student,Show_Student,Update_Student,Delete_Student )

urlpatterns = [
    path('add_stu/',Add_Student.as_view(),name='Add_Student'),
    path('show_stu/',Show_Student.as_view(),name='Show_Student'),
    path('update_stu/<int:pk>/',Update_Student.as_view(),name='Update_Student'),
    path('delete_stu/<int:pk>/',Delete_Student.as_view(),name='Delete_Student'),
]