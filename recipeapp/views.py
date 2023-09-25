from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from .forms import Applicantform

# Create your views here.
def index(request):
    recipes=Recipe.objects.all()
    context ={
        'recipes' : recipes
    }
    return render(request,'recipeapp/index.html',context)

def det(request,pk):
    recipe=Recipe.objects.get(pk=pk)
    if request.method=='POST':
        form=Applicantform(request.POST)
        if form.is_valid():
            taste=form.save(commit=False)
            taste.r=recipe
            taste.save()
    form=Applicantform()
    context ={
        'recipe' : recipe,
        'form' : form
    }
    return render(request,'recipeapp/det.html',context)