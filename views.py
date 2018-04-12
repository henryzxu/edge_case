from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Profile
from .forms import ProfileForm

class IndexView(generic.ListView):
    template_name = 'edge_case/index.html'
    context_object_name = 'edge_case_profiles'

    def get_queryset(self):
        return Profile.objects.order_by('name') 

def expand_profile(request, id):
    p = get_object_or_404(Profile, pk=id)
    return render(request, 'edge_case/profile.html', {'profile': p})

def submit_profile(request):
    p = ProfileForm()
    return render(request, 'edge_case/submit.html', {'form': p})

def submit(request):
    p = ProfileForm(request.POST, request.FILES)
    if p.is_valid():
        p.save()
        return HttpResponseRedirect(reverse('edge_case:index', args=()))
    else:
        p = ProfileForm()
    return render(request, 'edge_case/submit.html', {'form': p})

