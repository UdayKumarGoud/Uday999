from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import Http404
from .models import Employee
def employee_details(request,pk):
    # try:
    #     emp=Employee.objects.get(pk=pk)
    # print(emp)
    # except:
    #     raise Http404 

    emp=get_object_or_404(Employee,pk=pk)
    return render(request,"employee_detail.html")