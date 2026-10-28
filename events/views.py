from django.shortcuts import render
from .forms import EventRegistrationForm


def event_registration(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)

        if form.is_valid():
            registration = form.save()

            return render(
                request,
                "events/registration_success.html",
                {"registration": registration}
            )
    else:
        form = EventRegistrationForm()

    return render(
        request,
        "events/event_registration.html",
        {"form": form}
    )