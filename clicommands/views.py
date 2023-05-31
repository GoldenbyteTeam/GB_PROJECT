from django.shortcuts import redirect,get_object_or_404
from .forms import DefineCommandForm
from .models import Command


def add(request):
    if request.method == "POST":
        form = DefineCommandForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            if request.user.is_staff:
                form.instance.is_published = True
            form.save()
    return redirect('dashboard')

def edit(request,command_id):
    if request.method == "POST":
        command = get_object_or_404(Command, pk=command_id)
        form = DefineCommandForm(instance=command,data=request.POST)
        if form.is_valid():
            if request.user.is_staff:
                form.instance.is_published = True
            else:
                form.instance.is_published = False       # wait 4 review to publish again if not staff
            form.save()
    return redirect('dashboard')

def delete(request,command_id):
    if request.method == "POST":
        command = get_object_or_404(Command, pk=command_id)
        command.delete()
    return redirect('dashboard')



