from django.utils import timezone
from django_tables2   import RequestConfig
import django_tables2 as tables
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.module_loading import import_by_path
import django_filters

"""
These views do nothing other than provide members of the 'plain' Steroids template
set as default template names.
"""

from django.views import generic

class CreateView( generic.CreateView ):
    template_name = 'steroids/plain/form.html'
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['model'] = self.model
        return context

class UpdateView( generic.UpdateView ):
    template_name = 'steroids/plain/form.html'

class ListView( generic.ListView ):
    template_name = 'steroids/plain/list.html'

    def get_app(self):
        return models.get_app(ContentType.objects.get_for_model(self.model).app_label)

    def table(self):
        table_name = self.model.__name__ + "Table"
        print table_name
        try:
            Table = import_by_path(get_app().__name__[:-6] + "tables.%s" % table_name)
        except: pass
        try:
            Table = import_by_path(get_app().__name__[:-6] + "controls.%s" % table_name)
        except:
            class Table(tables.Table):
                actions = tables.TemplateColumn(template_name="steroids/actions_in_table.html", verbose_name="Acciones")
                class Meta:
                    model = self.model
                    attrs = {"class": "table"}

        model_table = Table(self.object_list, page_field="ppage")
        RequestConfig(self.request, paginate={"per_page": 25}).configure(model_table)
        return model_table

    def filters(self):
        filter_name = self.model.__name__ + "FilterSet"
        try:
            FilterSet = import_by_path(get_app().__name__[:-6] + "filtersets.%s" % filter_name)
        except: pass
        try:
            FilterSet = import_by_path(get_app().__name__[:-6] + "controls.%s" % filter_name)
        except:
            class FilterSet(django_filters.FilterSet):
                class Meta:
                    model = self.model
        model_filters = FilterSet(self.request.GET, queryset=self.object_list)
        self.object_list = model_filters.qs
        return model_filters


    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['filters'] = self.filters()
        context['table'] = self.table()
        return context

class DetailView( generic.DetailView ):
    template_name = 'steroids/plain/detail.html'

class DeleteView( generic.DeleteView ):
    template_name = 'steroids/plain/confirm_delete.html'
