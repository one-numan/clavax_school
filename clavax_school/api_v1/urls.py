"""
URL configuration for clavax_school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, add_student, update_student, update_student_patch, delete_student, all_class, home_page
from .views import StudentAPI, StudentViewSet  # Router and Views  Logic
from .views import add_new_class, add_new_student  # GUI Logic
from rest_framework import routers

studentRouter = routers.DefaultRouter()
studentRouter.register('', StudentViewSet)


urlpatterns = [
    # """Django Rest Framework Router"""
    path('api/v1/register/', include((studentRouter.urls, 'api_v1'), namespace='register')
         ),  # Register Page Task 1




    # """Class Based View"""
    path('api/v1/student/', StudentAPI.as_view(),
         name='student'),  # CRUD Operations



    # """Function Based View Authorization"""
    path('api/v1/class/', view=all_class, name='class'),


    # path('student/', view=add_student),
    # path('update_student/<int:id>/', view=update_student),
    # path('update_student_patch/<int:id>/', view=update_student_patch),
    # path('delete_student/<int:id>/', view=delete_student),

    # GUI Pages
    path('', view=home_page),
    path('student/', view=add_new_student, name='gui_student'),
    path('class/', view=add_new_class, name='gui_class'),




]
