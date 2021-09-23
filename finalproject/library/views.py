import re
from library.models import User
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from library.forms import SignUpForm,LoginForm
from library.models import Books
# Create your views here.

def index(request):
    return render(request, 'library/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'library/register.html',{"form":form , "msg": msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('adminpage')
            elif user is not None and user.is_student:
                login(request,user)
                return redirect('student-page')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request,'library/login.html',{"form":form , "msg": msg})

def admin(request):
    book_items = Books.objects.all()
    context = {"book_items":book_items}
    return render(request,'library/adminpage.html',context)

def student(request):
    book_items = Books.objects.all()
    context = {"book_items":book_items}
    return render(request,'library/student.html',context)

def studentFun(request):
    student_members = User.objects.all()
    data = {"student_members":student_members}
    return render(request,'library/studentmem.html',data)
    

def addbooks(request):
    if request.POST:
        bk = Books()
        bk.title = request.POST["title"]
        bk.author = request.POST["author"]
        bk.image = request.POST["image"]
        bk.status = request.POST["status"]
        bk.save()
        return redirect('adminpage')
    return render(request,'library/addnewbook.html')

def change_password(request):
    context = {}
    if request.method == "POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        user = User.objects.get(id = request.user.id)
        username = user.username
        password = new_pas
        check = user.check_password(current)
        if check == True:
            user.set_password(new_pas)
            user.save()
            authenticate(username=username, password=password)
            context["msg"] = "Password Changed Successfully"
            context["col"] = "alert-success"
        else:
            context["msg"] = "Incorrect Current Password"
            context["col"] = "alert-danger"
        # print(check)
    return render(request,'library/change-password.html',context)

def deleteBook(request,book_id):
    book_item = get_object_or_404(Books,pk = book_id)
    book_item.delete()
    return redirect('adminpage')
    #return HttpResponse(book_id)

def updateBook(request,book_id):
    book_item = get_object_or_404(Books,pk = book_id)
    if request.method == 'GET':
        context = {"book": book_item}
        return render(request,'library/update.html',context)
    elif request.method == 'POST':
        print(request.method)
        book_item.title = request.POST["title"]
        book_item.author = request.POST["author"]
        book_item.image = request.POST["image"]
        book_item.status= request.POST["status"]
        book_item.save()
        return redirect("adminpage")
    return HttpResponse(book_id)


def edit_profile(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        un = request.POST["username"]
        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.username = un
        usr.save()
        context["status"] = "Changes Saved Successfully"
    return render(request,"library/edit_profile.html", context)






# def borrowed_books(request):
#    borrowed_books = User.objects.all()
#    dataa = {"borrowed_books":borrowed_books}
#    return render(request,'library/borrow.html',dataa)