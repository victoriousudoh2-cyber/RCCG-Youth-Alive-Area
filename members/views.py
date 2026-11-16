
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MemberForm


def home(request):
    return render(request, "members/home.html")


def register_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your registration was submitted successfully!"
            )
            return redirect("register_member")

    else:
        form = MemberForm()

    return render(
        request,
        "members/register.html",
        {"form": form}
    )

    
