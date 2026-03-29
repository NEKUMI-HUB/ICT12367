from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import Person

# Create your views here.
def index(request):
    """
    Display the index page with all persons.
    """
    all_persons = Person.objects.all()
    return render(request,'index.html',{'all_persons': all_persons})

def about(request):
    """
    Display the about page.
    """
    return render(request,"about.html")

def form(request):
    """
    Handle the form for creating a new person.
    """
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST['name']
        age = request.POST['age']
        

# บันทึกข้อมูลลงฐานข้อมูล
        person = Person.objects.create(name=name, age=age)

# เปลี่ยนเส้นทางไปยหน้าแรก
        return redirect("/")
    else:

# แสดงฟอร์ม
        return render(request,"form.html")

def edit(request, id):
    """
    Handle editing an existing person.
    """
    person = get_object_or_404(Person, id=id)
    if request.method == "POST":
        person.name = request.POST['name']
        person.age = request.POST['age']
        person.save()
        return redirect("/")
    else:
        return render(request, "form.html", {'person': person})

def delete(request, id):
    """
    Delete a person by id.
    """
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect("/")