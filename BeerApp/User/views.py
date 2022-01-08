from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm
    if request.method == "POST":
        regiForm = UserCreationForm(request.POST)
        if regiForm.is_valid():
            regiForm.save()
            messages.success(request, "User has been registrated.")
        else:
            messages.error(request, "Something gone wrong")
    return render(request, "profile_create.html", {"form": form})
