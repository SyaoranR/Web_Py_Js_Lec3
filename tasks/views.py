from django.shortcuts import render

to_do = ["foo", "bar", "baz"]
# Create your views here.
def index(req):
    return render(req, "tasks/index.html", {
        "tasks": to_do
    })

def add(req):
    return render(req, "tasks/add.html")