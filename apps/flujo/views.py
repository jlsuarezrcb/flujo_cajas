from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import generic

from apps.flujo import models
from apps.flujo import forms
from django.contrib import messages

from apps.flujo.filters import ActivoFilter
from apps.flujo.mixins import SecurityMixin
from mail_templated import send_mail

from flujo_cajas.settings import EMAIL_HOST_USER


class Home(SecurityMixin,generic.TemplateView):
    template_name = 'home/login.html'

#activo
class ActivoView(SecurityMixin,generic.ListView):
    template_name = 'activo/listar_activos.html'
    context_object_name = "activos"
    model = models.Activo
    paginate_by = 10
    filter = None

    def get_queryset(self, **kwargs):
        filter = ActivoFilter(self.request.GET, queryset=super().get_queryset())
        self.filter = filter
        return filter.qs.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['frm_filter'] = self.filter.form
        pk = self.kwargs.get("pk")
        context['frm_activo'] = forms.FrmActivo(self.request.POST or None,
                                                instance=models.Activo.objects.filter(pk=pk).first())
        return context


class ActivoCreate(SecurityMixin,generic.CreateView):
    template_name = 'activo/form_activos.html'
    form_class = forms.FrmActivo
    models = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo_listar')


class ActivoUpdateView(SecurityMixin,generic.UpdateView):
    template_name = 'activo/form_activos.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        email="correo@gmail.com"
        send_mail('emails/activo.tpl', {'nombre':'jose luis','edad':35}, EMAIL_HOST_USER, [email])
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo_listar')


class ActivoDelete(SecurityMixin,generic.DeleteView):
    template_name = 'activo/delete_activo.html'
    model = models.Activo
    success_url = reverse_lazy('view_activo_listar')


#acreder
class AcredorView(SecurityMixin,generic.ListView):
    template_name = 'acredor/listar_acredor.html'
    context_object_name = "acredores"
    model = models.Acredor
    paginate_by = 10


class AcredorCreate(SecurityMixin,generic.CreateView):
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


class AcredorUpdateView(SecurityMixin,generic.UpdateView):
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


class AcredorDelete(SecurityMixin,generic.DeleteView):
    template_name = 'activo/delete_activo.html'
    model = models.Acredor
    success_url = reverse_lazy('view_acredor_listar')


#categoria
class CategoriaView(SecurityMixin,generic.ListView):
    template_name = 'categoria/listar_categorias.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Categoria  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'categorias'
    paginate_by = 4


class CategoriaCreateView(SecurityMixin,generic.CreateView):
    template_name = 'categoria/form_categoria.html'
    form_class = forms.FrmCategoria
    model = models.Categoria

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_categoria_listar')


class CategoriaUpdateView(SecurityMixin,generic.UpdateView):
    template_name = 'categoria/form_categoria.html'
    form_class = forms.FrmCategoria
    model = models.Categoria

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_categoria_listar')


class CategoriaDelete(SecurityMixin,generic.DeleteView):
    template_name = 'categoria/delete_categoria.html'
    model = models.Categoria
    success_url = reverse_lazy('view_categoria_listar')


#subcategoria
class SubCategoriaView(SecurityMixin,generic.ListView):
    template_name = 'subcategoria/listar_subcategorias.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.SubCategoria  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'subcategorias'
    paginate_by = 4


class SubCategoriaCreateView(SecurityMixin,generic.CreateView):
    template_name = 'subcategoria/form_subcategoria.html'
    form_class = forms.FrmSubCategoria
    model = models.SubCategoria

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_subcategoria_listar')


class SubCategoriaUpdateView(SecurityMixin,generic.UpdateView):
    template_name = 'subcategoria/form_subcategoria.html'
    form_class = forms.FrmSubCategoria
    model = models.SubCategoria

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_subcategoria_listar')


class SubCategoriaDelete(SecurityMixin,generic.DeleteView):
    template_name = 'subcategoria/delete_subcategoria.html'
    model = models.SubCategoria
    success_url = reverse_lazy('view_subcategoria_listar')


#obligaciones
class ObligacionesView(SecurityMixin,generic.ListView):
    template_name = 'obligaciones/listar_obligaciones.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Obligaciones  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'obligaciones'
    paginate_by = 4


class ObligacionesCreateView(SecurityMixin,generic.CreateView):
    template_name = 'obligaciones/form_obligacion.html'
    form_class = forms.FrmObligaciones
    model = models.Obligaciones

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_obligaciones_listar')


class ObligacionesUpdateView(SecurityMixin,generic.UpdateView):
    template_name = 'obligaciones/form_obligacion.html'
    form_class = forms.FrmObligaciones
    model = models.Obligaciones

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_obligaciones_listar')


class ObligacionesDelete(SecurityMixin,generic.DeleteView):
    template_name = 'obligaciones/delete_obligacion.html'
    model = models.Obligaciones
    success_url = reverse_lazy('view_obligaciones_listar')


#class Contacto(generic.TemplateView):
#    template_name = 'home/contacto.html'

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data()
    #    return context
