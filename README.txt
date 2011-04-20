Haystack Demo @ CustomMade.com

What?
Why?

Possible Topics:
    Install
    Facets
    Advanced Views
    Data Preparation
    Advanced Views
    Scaling

Links:
    http://haystacksearch.org


    Solr
        http://wiki.apache.org/solr/SolrTomcat
        http://www.tc.umn.edu/~brams006/solr_ubuntu.html

Shell Commands Used:
rm schema.xml && ./manage.py build_solr_schema >> schema.xml
sudo cp schema.xml /usr/share/tomcat6/demo/conf/
time python manage.py rebuild_index

