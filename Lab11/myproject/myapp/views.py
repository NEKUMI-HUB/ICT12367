from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_persons = Person.objects.all()
    return render(request,'index.html',{'all_persons': all_persons})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        

# บันทึกข้อมูลลงฐานข้อมูล
        person = Person(name=name, age=age)
        person.save()

# เปลี่ยนเส้นทางไปยหน้าแรก
        return redirect("/")
    else:

# แสดงฟอร์ม
        return render(request,"form.html")

def edit(request, id):
    person = Person.objects.get(id=id)
    if request.method == "POST":
        person.name = request.POST['name']
        person.age = request.POST['age']
        person.save()
        return redirect("/")
    else:
        return render(request, "form.html", {'person': person})

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/")