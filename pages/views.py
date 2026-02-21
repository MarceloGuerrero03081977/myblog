from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm


# Vista home (función)
def home(request):
    latest_pages = Page.objects.all()[:3]
    return render(request, 'home.html', {'latest_pages': latest_pages})


# Vista about (función)
def about(request):
    return render(request, 'about.html')


# CBV - Lista de páginas
class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


# CBV - Detalle de página
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'


# CBV - Crear página (con Mixin)
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Página creada exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Crear'
        return context


# CBV - Editar página (con Mixin)
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Editar'
        return context


# CBV - Eliminar página (con Mixin)
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/confirm_delete.html'
    success_url = reverse_lazy('page_list')
    context_object_name = 'page'

    def form_valid(self, form):
        messages.success(self.request, 'Página eliminada.')
        return super().form_valid(form)