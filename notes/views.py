from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, Http404
from django.db.utils import IntegrityError
from .forms import LoginForm, RegistrationForm
from .models import UserModel
import hashlib

# Create your views here.


def home(request):
    userAgent = request.headers['User-Agent']
    print("Usder agent:", userAgent)
    print("User agent header:", userAgent)
    USER_OPERATING_SYSTEM = "UNRECOGNIZED"

    if "Windows" in userAgent:
        USER_OPERATING_SYSTEM = "Windows"
    elif "Android" in userAgent:
        USER_OPERATING_SYSTEM = "Android"
    elif "Linux x86_64" in userAgent:
        USER_OPERATING_SYSTEM = "LINUX"
    elif "PostmanRuntime" in userAgent:
        USER_OPERATING_SYSTEM = "POSTMAN API testing service"
    else:
        print("Unknown operating system detected!!")

    login_form = LoginForm()
    registration_form = RegistrationForm()
    return render(request, "login.html", {
        "os": USER_OPERATING_SYSTEM,
        "login_form": login_form,
        "registration_form": registration_form
    })


def newUserRegistration(request):
    fields = RegistrationForm.declared_fields.keys()
    print("All fields", fields)
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        data = {i: form.cleaned_data.get(i) for i in fields}
    if data['password'] != data['re_password']:
        return redirect('')
        # form_data = form.cleaned_data
    print(data)
    obj = UserModel(fullname=data['fullname'], username=data['username'],
                    password=data['password'], email=data['email'])
    try:
        obj.save()
    except IntegrityError:
        return render(request, "loginpage_message.html", {
            "message": "Already registered",
            "messageColor": "red",
            "sub_message": "Existing user"
        })
    return render(request, "loginpage_message.html", {
        "message": "Successfully registered",
        "messageColor": "lightgreen",
        "sub_message": ""
    })


def login(request):
    fields = LoginForm.declared_fields.keys()
    print("All fields:", fields)
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = {i: form.cleaned_data.get(i) for i in fields}
    print(data)
    data['username'] = hashlib.sha3_256(
        data['username'].encode('utf-8')).hexdigest()
    data['password'] = hashlib.sha3_256(data['password'].encode('utf-8')).hexdigest()
    obj = UserModel.objects.get(
        username=data['username'], password=data['password'])
    print("Object:", obj)
    if obj.isActive:
        if obj is not None:
            if not request.session.exists(request.session.session_key):
                request.session.create() 
            return HttpResponse("Data:"+str(data)+"<br>User is valid"+"<br>"+request.session.session_key)
    return HttpResponse("Data:"+str(data)+"<br>")
