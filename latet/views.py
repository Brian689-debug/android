from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from rest_framework.serializers import Serializer

from latet.models import students
from latet.serializers import StudentSerializer


# Create your views here.
def index(request):
    data = students.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)
def about(request):
    data = students.objects.all()
    context = {'data': data}
    return render(request, 'about.html')

def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        form = students(name=name, email=email, age=age, location=location, gender=gender)
        form.save()
        return redirect('/')
    return render(request, 'index.html')

def editstudents(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        location = request.POST.get('location')
        gender = request.POST.get('gender')

        editForm = students.objects.get(id=id)
        editForm.name = name
        editForm.email = email
        editForm.age = age
        editForm.location = location
        editForm.gender = gender
        editForm.save()
        return redirect('/')
    student = students.objects.get(id=id)
    context = {'student': student}
    return render(request, 'edit.html', context)

def deletestudents(request, id):
    student = students.objects.get(id=id)
    student.delete()
    return redirect('/')

def student_list(request):
    student = students.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)

def mpesaapi(request):
    cl = MpesaClient()
    phone_number = '0787536789'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'http//darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference,  transaction_desc, callback_url)

    return HttpResponse(response)
def stk_push_callback(request):
    data = request.body
    return HttpResponse('STK PUSH has been sent successfully')





















