from django.shortcuts import render, get_object_or_404, redirect

from .forms import AmbassadorForm

from .models import Story, StoryImage


# Create your views here.

def home(request):
    return render(request, 'home.html')


def stories(request):
    stories = Story.objects.all()  # Get all stories
    return render(request, 'stories.html', {'stories': stories})


def form(request):
    if request.method == 'POST':
        form = AmbassadorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('app:form')
    else:
        form = AmbassadorForm()

    return render(request, 'form.html', {'form': form})
