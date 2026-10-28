from django.shortcuts import render,redirect
from .models  import Member
from .forms  import MemberForm

# Create your views here.
def home(request):
    return render(request, "members/home.html")


def register_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)  

        if form.is_valid():
            form.save()
            return redirect("register_member")

    else:
        form = MemberForm()

        return render(request,"members/register.html", {"form":form})

    