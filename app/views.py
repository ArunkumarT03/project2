from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request,'form.html')
def list1(request):
    return render(request,'list.html')