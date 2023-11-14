from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import Usuarioforms, CommentForm
from .models import Comment

# Create your views here.

def addcomment(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.save()

            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

def index(request):
    return render(request, 'index.html')

class UsuarioCreate(CreateView):
    form_class = Usuarioforms
    template_name = 'usuario/registrar.html'
    success_url = reverse_lazy ('login')
