from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

class regclass(generic.CreateView):
    form_class = regform
    template_name = 'reg.html'
    success_url = reverse_lazy('login')

# reverse_lazy is used to redirect the url after successfull completeion of registration..(redirection url)

class logclass(generic.View):
    form_class = logform
    template_name = 'log.html'
    def get(self, request):
        a = logform
        return render(request, 'log.html', {'form': a})
    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            b = regmodel.objects.all()
            for i in b:
                if i.email == email and i.password == password:
                    return HttpResponse('Login Succesfull')
            else:
                return HttpResponse('Login Failed')

class studentreg(generic.CreateView):
    form_class = studentform
    template_name = 'StudentReg.html'
    success_url = reverse_lazy('studentdisplay')

class studentdisplay(generic.ListView):
     model = StudentDetails
     template_name = 'StudentDisplay.html'
     context_object_name = 'data'

class delete_stud(generic.DeleteView):
    model = StudentDetails
    template_name = 'StudentDelete.html'
    success_url = reverse_lazy('studentdisplay')

class detail_stud(generic.DetailView):
    model = StudentDetails
    template_name = 'Student.html'

# object.field is used to access data from database in html page. eg: object.student_name not data.

class update_stud(generic.UpdateView):
    model = StudentDetails
    fields = ['student_name', 'image', 'dob', 'email', 'maths_score', 'Physics_score', 'Chemistry_score']
    template_name = 'StudentUpdate.html'
    success_url = reverse_lazy('studentdisplay')


class fileupload(generic.CreateView):
    form_class = itemform
    template_name = 'Fileupload.html'
    success_url = reverse_lazy('displayfile')

class displayfile(generic.ListView):
    model = Uploadimage
    template_name = 'DisplayFile.html'
    context_object_name = 'data'

class deletefile(generic.DeleteView):
    model = Uploadimage
    template_name = 'DeleteFile.html'
    success_url = reverse_lazy('displayfile')


class detailfile(generic.DetailView):
    model = Uploadimage
    template_name = 'FileDetail.html'

class updatefile(generic.UpdateView):
    model = Uploadimage
    fields = ['itemname', 'image']
    template_name = 'UpdateFile.html'
    success_url = reverse_lazy('displayfile')




