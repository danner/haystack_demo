from django.conf.urls.defaults import *

import haystack.views

urlpatterns = patterns('',
    (r'^$', haystack.views.SearchView(template='search.html')),
)
