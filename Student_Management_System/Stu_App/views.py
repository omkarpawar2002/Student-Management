from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student

class Add_Student(View):
    template_name = 'Stu_App/Add_Student.html'

    def get(self,request):
        form = StudentForm()
        context = {'form':form}
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
        return HttpResponse("Something Went Wrong")
    
class Show_Student(View):
    template_name = 'Stu_App/Show_Student.html'

    def get(self,request):
        objs = Student.objects.all()
        context = {'records':objs}
        return render(request,self.template_name,context)
    
class Update_Student(View):
    template_name = 'Stu_App/Update_Student.html'

    def get_object(self,pk):
        return get_object_or_404(Student,stu_id=pk)

    def get(self,request,pk):
        obj = self.get_object(pk)
        form = StudentForm(instance=obj)
        context = {'form':form}
        return render(request,self.template_name,context)
        
    def post(self,request,pk):
        obj = self.get_object(pk)
        form = StudentForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
        return HttpResponse("Something Went Wrong While Updating Details")
    
class Delete_Student(View):
    template_name = 'Stu_App/Delete_Student.html'

    def get_object(self,pk):
        return get_object_or_404(Student,stu_id=pk)

    def get(self,request,pk):
        obj = self.get_object(pk)
        form = StudentForm(instance=obj)
        context = {'obj':obj}
        return render(request,self.template_name,context)
    
    def post(self,request,pk):
        obj = self.get_object(pk)
        obj.delete()
        return redirect('Show_Student')