from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

from steroids import views as steroids_views

class URLGenerator( object ):
    """
    Constructs and returns CRUD urls for generic Steroids views for a given model.

    URL names follow the pattern: <lower case model name>_<action>
        - ``lowercasemodelname_detail``: For the DetailView.
        - ``lowercasemodelname_create``: For the CreateView.
        - ``lowercasemodelname_list``:   For the ListView.
        - ``lowercasemodelname_update``: For the UpdateView.
        - ``lowercasemodelname_delete``: For the DeleteView.
    """

    def __init__( self, model, steroids_view_prefix = None ):
        """
        Internalize the model and set the view prefix.
        """
        self.model = model
        self.steroids_view_prefix = steroids_view_prefix or model.__name__.lower()

    def get_create_url( self, **kwargs ):
        """
        Generate the create URL for the model.
        """
        return url(
            r'%s/create/$' % self.steroids_view_prefix,
            steroids_views.CreateView.as_view( model = self.model, **kwargs ),
            name = '%s_create' % self.steroids_view_prefix,
        )

    def get_update_url( self, **kwargs  ):
        """
        Generate the update URL for the model.
        """
        return url(
            r'%s/update/(?P<pk>\d+)$' % self.steroids_view_prefix,
            steroids_views.UpdateView.as_view( model = self.model, **kwargs ),
            name = '%s_update' % self.steroids_view_prefix,
        )

    def get_list_url( self, **kwargs ):
        """
        Generate the list URL for the model.
        """
        return url(
            r'%s/list$' % self.steroids_view_prefix,
            steroids_views.ListView.as_view( model = self.model, **kwargs ),
            name = '%s_list' % self.steroids_view_prefix,
        )

    def get_delete_url( self, **kwargs ):
        """
        Generate the delete URL for the model.
        """
        return url(
            r'%s/delete/(?P<pk>\d+)$' % self.steroids_view_prefix,
            steroids_views.DeleteView.as_view(
               model = self.model,
                success_url = reverse_lazy('%s_list' % self.steroids_view_prefix),
                **kwargs
            ),
            name = '%s_delete' % self.steroids_view_prefix,
        )

    def get_detail_url( self, **kwargs ):
        """
        Generate the detail URL for the model.
        """
        return url(
            r'%s/(?P<pk>\d+)$' % self.steroids_view_prefix,
            steroids_views.DetailView.as_view( model = self.model, **kwargs ),
            name = '%s_detail' % self.steroids_view_prefix,
        )

    def get_urlpatterns( self, paginate_by = 10 ):
        """
        Generate the entire set URL for the model and return as a patterns
        object.
        """
        return patterns( '',
            self.get_create_url(),
            self.get_update_url(),
            self.get_list_url( paginate_by = paginate_by ),
            self.get_delete_url(),
            self.get_detail_url()
        )
