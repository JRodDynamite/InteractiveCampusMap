from django.conf.urls import url, patterns
from map import views

urlpatterns = patterns('',
    url(r'^$',views.All),
    url(r'^(?P<buildingname>.*)/$',views.SpecificBuilding),
    )
