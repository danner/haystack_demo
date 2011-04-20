from haystack.forms import FacetedSearchForm

class FacetSearchForm(FacetedSearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()
