from django.http import HttpResponse
from django.shortcuts import render
from.models import Person



# Create your views here.
def demo(request):
    # obj=Fruit.objects.all()

    obj1=Person.objects.all()
    return render(request, 'index.html', {'new': obj1})







