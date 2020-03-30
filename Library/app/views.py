# imports required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import  messages
from app.models import  *
from datetime import datetime, timedelta
from django.contrib.auth.decorators import  login_required




# home page
@login_required()
def index(request):
    return render(request,"app/index.html",{})


# users urls
# login page
def login_page(request):
    return render(request,"app/login.html",{})

# login function
def login_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect("app:index")
    else:
        messages.info(request,"username or password incorrect[login failed]")
        return redirect("app:login_page")

# logout function
@login_required()
def logout_view(request):
    logout(request)
    messages.info(request,"[logout success]")
    return redirect("app:login_page")

# signup page
def signup_page(request):
    if request.user.is_authenticated==True:
        return render(request,"app/index.html",{})
    else:
        return render(request,"app/signup.html",{})

# signup function
def signup_view(request):
    if request.method=='POST'and request.FILES['picture']:
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        image=request.FILES['picture']
        slug=request.POST['slug']
        if User.objects.filter(username=username):
            messages.info(request,"faild ..user already exists")
            return redirect("app:signup_page")
        elif User.objects.filter(email=email):
            messages.info(request,"failed...email already taken")
            return redirect("app:signup_page")
        elif password1!=password2:
            messages.info(request,"failed...password not mached")
            return redirect("app:signup_page")
        else:
            user=User.objects.create_user(username=username,email=email,password=password2,picture=image,slug=slug)
            user.save();
            messages.info(request,"signup successful")
            return redirect("app:login_page")
    else:
        return redirect("app:signup_page")

# reset page
def reset_page(request):
    return render(request,"app/reset.html")

# reset function
def reset_password_view(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        res=User.objects.filter(email=email)
        if res:
            user=User.objects.get(email=email)
            user.set_password(password)
            user.save();
            messages.info(request,"password reset successful")
            return redirect("app:login_page")
        else:
            messages.info(request,"email not matched")
            return redirect("app:reset_page")
    else:
        return redirect("app:reset_page")

@login_required()
def update_profile_page(request):
    return render(request,"app/update_profile_page.html")

@login_required()
def update_profile(request,slug):
    user=User.objects.get(slug=slug)
    if request.method=='POST'and request.FILES['picture']:
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        image=request.FILES['picture']
        username=username
        user.email=email
        user.phone=phone
        user.address=address
        user.picture=image
        user.save()
        return redirect("app:index")

##### book functions
@login_required()
def book_display(request):
    books=Book.objects.all()
    context={
        'books':books,
        }
    return render(request,"app/books.html",context)

@login_required()
def new_book_page(request):
    return render(request,"app/create.html")

@login_required()
def update_page(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,"app/update.html",{'book':book})

@login_required()
def del_page(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,"app/del_page.html",{'book':book})

@login_required()
def new_book(request):
    if request.method=="POST":
        code=request.POST['code']
        name=request.POST['name']
        author=request.POST['author']
        publisher=request.POST['publisher']
        type=request.POST['type']
        slug=request.POST['slug']
        book=Book(code=code,name=name,author=author,publisher=publisher,type=type,slug=slug)
        book.save()
        return redirect("app:book_display")
    else:
        return redirect("app:new_book_page")

@login_required()
def update(request,slug):
    if request.method=="POST":
        code=request.POST['code']
        name=request.POST['name']
        author=request.POST['author']
        publisher=request.POST['publisher']
        type=request.POST['type']
        book=Book.objects.get(slug=slug)
        book.code=code
        book.name=name
        book.author=author
        book.publisher=publisher
        book.type=type
        book.save()
        return redirect("app:book_display")
    else:
        return redirect("app:update_page")

@login_required()
def delete(request,slug):
    if request.method=="POST":
        book=Book.objects.get(slug=slug).delete()
        return redirect("app:book_display")
    else:
        return redirect("app:book_display")

@login_required()
def issue_page(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,"app/issue_page.html",{'book':book})

@login_required()
def issue(request,slug):
    if request.method=="POST":
        book=Book.objects.get(slug=slug)
        book.issued=True
        book.issue_date=datetime.now()
        book.due_date=book.issue_date+ timedelta(hours=168)
        book.save()
        return redirect("app:book_display")
    else:
        return redirect("app:book_display")

@login_required()
def del_issue_page(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,"app/del_issue_page.html",{'book':book})

@login_required()
def del_issue(request,slug):
    if request.method=="POST":
        book=Book.objects.get(slug=slug)
        book.issued=False
        book.issue_date=None
        book.due_date=None
        book.save();
        return redirect("app:book_display")
    else:
        return redirect("app:book_display")

# create database

@login_required()
def create_data_page(request):
    return render(request,"app/create_data_page.html")

@login_required()
def create_data(request,num):
    from faker import Faker
    faker=Faker()
    num=int(num)
    for i in range(1,num):
        b=Book(code=faker.zipcode(),name=faker.company(),author=faker.city(),publisher=faker.company(),slug=faker.slug(),type="computer",issued=False)
        b.save();
    return redirect("app:book_display")

@login_required()
def staff_page(request):
    if request.user.is_superuser:
        users=User.objects.all()
        return render(request,"app/staff.html",{'users':users})
    else:
        messages.info(request,"you should be a staff admin")
        return redirect("app:index")

@login_required()
def new_staff_page(request):
    return render(request,"app/new_staff_page.html")

@login_required()
def delete_staff_page(request,slug):
    user=User.objects.get(slug=slug)
    return render(request,"app/delete_staff_page.html",{'user':user})

@login_required()
def update_staff_page(request,slug):
    user=User.objects.get(slug=slug)
    return render(request,"app/update_staff_page.html",{'user':user})

@login_required()
def new_staff(request):
    if request.method=='POST'and request.FILES['picture']:
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        image=request.FILES['picture']
        status=request.POST['is_admin_status']
        slug=request.POST['slug']
        if User.objects.filter(username=username):
            messages.info(request,"faild ..user already exists")
            return redirect("app:signup_page")
        elif User.objects.filter(email=email):
            messages.info(request,"failed...email already taken")
            return redirect("app:signup_page")
        elif password1!=password2:
            messages.info(request,"failed...password not mached")
            return redirect("app:signup_page")
        else:
            user=User.objects.create_user(username=username,email=email,password=password2,picture=image,slug=slug)
            if status=="True":
                user.is_superuser=True
                user.is_staff=True
            else:
                user.is_superuser=False
                user.is_staff=False
            user.save();
            messages.info(request,"signup successful",status)
            return redirect("app:staff_page")
    else:
        messages.info(request,"signup failed",status)
        return redirect("app:signup_page")

@login_required()
def update_staff(request,slug):
    user=User.objects.get(slug=slug)
    if request.method=='POST'and request.FILES['picture']:
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        image=request.FILES['picture']
        status=request.POST['is_admin_status']
        print(status)
        username=username
        user.email=email
        user.phone=phone
        user.address=address
        user.picture=image
        if status=="True":
            user.is_superuser=True
            user.is_staff=True
        else:
            user.is_superuser=False
            user.is_staff=False
        user.save()
        return redirect("app:staff_page")


@login_required()
def delete_staff(request,slug):
    if request.method=="POST":
        User.objects.get(slug=slug).delete()
        return redirect("app:staff_page")
    else:
        return redirect("app:staff_page")


