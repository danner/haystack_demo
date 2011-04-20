from django.conf.urls.defaults import *

import school.views
import school.forms
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().facet('school')

urlpatterns = patterns('',
    (r'^$', school.views.FacetSearchView(form_class=school.forms.FacetSearchForm, searchqueryset=sqs, template='search.html')),
)
