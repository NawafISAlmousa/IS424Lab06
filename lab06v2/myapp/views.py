from django.shortcuts import render,HttpResponseRedirect,reverse
from . import models
from django import forms

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = models.Student
        fields = ['sid','firstName','lastName','age']




class CourseForm(forms.ModelForm):

    class Meta:
        model = models.Course
        fields = '__all__'

def studentCourseAdd(request, sid):
    if request.method == "POST":

        stud = models.Student.objects.get(pk=sid)

        cid = str(request.POST["course"])

        course = models.Course.objects.get(pk=cid)

        stud.courses.add(course)

        return HttpResponseRedirect(reverse("details", args=(sid)))


def students(request):
    if request.method == "POST":

        form=StudentForm(request.POST)

        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("myapp:students"))
    
    studentslist = models.Student.objects.all()
    
    return render(request, "myapp/students.html", {"studs" : studentslist,
        "form": StudentForm()}
    )

def courses(request):
        
        if request.method == "POST":
            form =CourseForm(request.POST)
            if(form.is_valid):
                form.save()
                return HttpResponseRedirect(reverse("myapp:courses"))
        
        courseslist = models.Course.objects.all()
        
        return render(request, "myapp/courses.html", {"courses" : courseslist,
            "form": CourseForm()}
    )

def details(request, sid):
    if request.method == "POST":

        stud = models.Student.objects.get(pk=sid)

        cid = request.POST["course"]

        course = models.Course.objects.get(pk=cid)

        stud.courses.add(course)

        return HttpResponseRedirect(reverse("myapp:details", args=(sid,)))
    stud = models.Student.objects.get(pk=sid)

    added_courses = stud.courses.all()

    free_courses = models.Course.objects.exclude(students=stud).all()

    return render(request, "myapp/details.html",{
        "stud": stud,
        "added_courses": added_courses,
        "free_courses": free_courses
    })
    
# Create your views here.
