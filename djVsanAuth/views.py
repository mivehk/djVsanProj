from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from djVsanCapacity.models import Clusters

# Create your views here.
@login_required
def dashboard(request):
	cluster_list = Clusters.objects.filter(user=request.user)
	return render(request, 'djVsanCapacity/index.html', {'cluster_list': cluster_list})
    #return render(request, 'djVsanCapacity/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


