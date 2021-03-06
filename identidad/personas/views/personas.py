"""Personas views."""

# Django
from django.views.generic import FormView

"""Archivo de vistas para personas."""

# Filters
from identidad.personas.filters import PersonasFilter

# Views
from django.views.generic import ListView

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from identidad.personas.models import Personas

class PersonasListView(LoginRequiredMixin, ListView):
    """Lista de personas""" 

    model = Personas
    ordering = ('-username',)
    template_name = 'personas/search.html'
    context_object_name = 'personas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PersonasFilter(self.request.GET, queryset=self.get_queryset())
        return context
