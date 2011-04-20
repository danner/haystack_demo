from haystack.views import SearchView
from haystack.query import SearchQuerySet

class FacetSearchView(SearchView):
    __name__ = 'FacetSearchView'
    def extra_context(self):
        return {
            'request': self.request,
            'facets': self.results.facet_counts(),
        }
