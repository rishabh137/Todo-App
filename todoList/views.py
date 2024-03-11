from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Todo
from django.urls import reverse

# Create your views here.
def index(request):
    all_list = Todo.objects.all()
    if request.method == "POST":
        itemVal = request.POST['input']
        data = Todo(item= itemVal)
        data.save()
    return render(request, "todoList/index.html", {"all_list": all_list})

def delete(request, id):
    list = Todo.objects.get(id=id)
    list.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def update(request, id):
    list = Todo.objects.get(id=id)
    # template = loader.get_template("update.html")
    context = {
        'mymember': list
    }
    return render(request, "todoList/update.html", context)

def updaterecord(request, id):
    itemVal = request.POST['input']
    member = Todo.objects.get(id = id)
    member.item = itemVal
    member.save()
    return HttpResponseRedirect(reverse('todo:index'))