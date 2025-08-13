from django.shortcuts import render, get_object_or_404, redirect

from .forms import AmbassadorForm



# Create your views here.

def home(request):
    return render(request, 'home.html')


def stories(request):
    return render(request, 'stories.html')

def form(request):
    if request.method == 'POST':
        form = AmbassadorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('app:form')
    else:
        form = AmbassadorForm()

    return render(request, 'form.html', {'form': form})

