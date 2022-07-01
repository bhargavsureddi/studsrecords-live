from django.shortcuts import render,get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student
from .filters import StudentFilter
from django.contrib.auth.decorators import login_required

def studhome(request):
    return render(request,"student/home.html")
@login_required
def show(request):
    ordering = ["year",'class_signature',"roll_no"]
    filter=StudentFilter(request.GET,Student.objects.all().order_by(*ordering))
    object_list=filter.qs
    context={"object_list":object_list,"filter":filter}
    return render(request,"student/record_filters.html",context=context)


class RecordsListView(LoginRequiredMixin,ListView):
    model=Student
    paginate_by = 5
    ordering = ["year",'class_signature',"roll_no"]

class RecordsByYearsListView(LoginRequiredMixin,ListView):
    model=Student
    template_name = "student/filtered.html"
    paginate_by = 5
    def get_queryset(self):
        yearReq=self.kwargs["year"]
        orderByList=["class_signature","roll_no"]
        return Student.objects.filter(year=yearReq).order_by(*orderByList)

class RecordsDetailView(LoginRequiredMixin,DetailView):
    model = Student

class RecordCreateView(LoginRequiredMixin,CreateView):
    model = Student
    fields = "__all__"

class RecordUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("records-list")
    
class RecordDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    success_url = reverse_lazy("records-list")
