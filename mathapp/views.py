from django.shortcuts import render

# Create your views here.

def get_addition_page(request):
    return render(request,'mathapp/addition.html')

def calculate(request):
    num1 = int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1+num2
    # print(res)
    context = {}
    context['result']=res
    return render(request,'mathapp/addition.html',context)

def get_sub_page(request):
    return render(request,'mathapp/sub.html')

def substraction(request):
    num1 = int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1-num2
    context={}
    context['result']=res
    return render(request,'mathapp/sub.html',context)

def get_mul_page(request):
    return render(request,'mathapp/multiplication.html')

def multiplication(request):
    num1 = int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1*num2
    context = {}
    context['result']=res
    return render(request,'mathapp/multiplication.html',context)

def get_div_page(request):
    return render(request,'mathapp/division.html')

def division(request):
    num1 = int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1/num2
    context = {}
    context['result'] = res
    return render(request,'mathapp/division.html',context)

