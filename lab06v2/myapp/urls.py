from django.urls import path
from .  import views 

app_name = "myapp"

urlpatterns = [
    path("students/", views.students, name= "students"),
    path("courses/", views.courses, name= "courses"),
    path("details/<str:sid>", views.details, name= "details")
]