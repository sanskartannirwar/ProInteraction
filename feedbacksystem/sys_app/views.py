from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Signupform, Contactdetails, Feedbackform
from django.contrib.auth.forms import AuthenticationForm     # for signin view
from django.contrib.auth import authenticate, login, logout   # for login in properly
from .models import Feedback, Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def course(request):
    return render(request, 'courses.html')


def python(request):
    return render(request, 'python.html')


def java(request):
    return render(request, 'java.html')


def moduler(request):
    return render(request, 'moduler.html')


def contact(request):
    if request.method == 'POST':
        ct = Contactdetails(request.POST)
        if ct.is_valid():
            name = ct.cleaned_data['name']
            email = ct.cleaned_data['email']
            mobile_number = ct.cleaned_data['mobile_number']
            course = ct.cleaned_data['course']
            address = ct.cleaned_data['address']
            Contact.objects.create(name=name, email=email, mobile_number=mobile_number, course=course, address=address)
        return redirect('contact')
    else:
        ct = Contactdetails()
        dt = Contact.objects.all()
    return render(request, 'contact.html', {'contact': ct, 'details': dt})



def signup(request):
    if request.method == "POST":
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have register successfully.')
            return redirect("/signin")
    else:
        fm = Signupform()
    return render(request, 'signup.html', {'signin': fm})




def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            # feed = FeedbackEntry()
            if user is not None:
                login(request, user)
                return render(request, 'home.html', {'user': user, })
                # return redirect("/feedback")

    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})



def feedback(request):
    if request.method == 'POST':
        fd = Feedbackform(request.POST)
        if fd.is_valid():
            if not request.user.is_authenticated:
                # Redirect to the login page if the user is not authenticated
                return redirect('signin')
            fd.save()
            return redirect('feedback')
    else:
        fd = Feedbackform()
    show = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': fd, 'show': show})


def showfeedback(request):
    show = Feedback.objects.all()
    return render(request, 'reviews.html', {'show': show})







def signout(request):
    logout(request)
    return redirect("home")


def your_view(request):
    user = request.user
    return render(request, 'home.html', {'user': user})