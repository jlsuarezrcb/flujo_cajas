from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic

from apps.flujo import models
from apps.flujo import forms


class Home(generic.TemplateView):
    template_name = 'home/login.html'


class ActivoView(generic.ListView):
    template_name = 'activo/form_activos.html'
    context_object_name = "activos"
    model = models.Activo
    paginate_by = 10


class ActivoCreate(generic.CreateView):
    template_name = 'activo/listar_activos.html'
    form_class = forms.FrmActivo
    models = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo_listar')


class ActivoUpdateView(generic.UpdateView):
    template_name = 'activo/listar_activos.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo_listar')


class AcredorView(generic.ListView):
    template_name = 'acredor/listar_acredor.html'
    context_object_name = "acredores"
    model = models.Acredor
    paginate_by = 10


class AcredorCreate(generic.CreateView):
    template_name = 'acredor/form_acredor.html'
    form_class = forms.FrmAcredor
    models = models.Acredor

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_acredor_listar')


class AcredorUpdateView(generic.UpdateView):
    template_name = 'acredor/form_acredor.html'
    form_class = forms.FrmAcredor
    model = models.Acredor

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_acredor_listar')


class Contacto(generic.TemplateView):
    template_name = 'home/contacto.html'

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data()
    #    return context
