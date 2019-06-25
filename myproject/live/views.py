from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Live
from .forms import LiveForm


def live_list(request):
    lives = Live.objects.all()
    context = {'object_list': lives}
    template_name = 'live/live_list.html'
    return render(request, template_name, context)


def live_add(request):
    form = LiveForm()
    context = {'form': form}
    template_name = 'live/live_form.html'
    return render(request, template_name, context)


class LiveCreateView(CreateView):
    model = Live
    form_class = LiveForm
    template_name = 'live/live_form.html'
    success_url = reverse_lazy('live:live_list')


def live_json(request):
    lives = Live.objects.all()
    data = [live.to_dict_json() for live in lives]
    return JsonResponse({'data': data})
