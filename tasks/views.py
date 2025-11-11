from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# to_do = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(
    #     label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(req):
    if "tasks" not in req.session:
        req.session["tasks"] = []
    return render(req, "tasks/index.html", {
        # "tasks": to_do
        "tasks": req.session["tasks"]
    })

def add(req):
    if req.method == "POST":
        form = NewTaskForm(req.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # to_do.append(task)
            req.session["tasks"] += [task]
            # return HttpResponseRedirect("/tasks")
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(req, "tasks/add.html", {
                "form": form
            })

    return render(req, "tasks/add.html", {
        "form": NewTaskForm()
    })