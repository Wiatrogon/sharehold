from django.conf.urls import url
from circulation import views

urlpatterns = [
    # client links
    url(r'^rClient/$', views.RentalClientListView.as_view(), name='circulation_entries'),
    url(r'^rClient/new/$', views.RentalClientCreateView.as_view(), name='rentalClient_new'),
    url(r'^rClient/(?P<pk>\d+)/edit/$', views.ClientUpdateView.as_view(), name='rentalclient_edit'),
    url(r'^rClient/new/return_home', views.return_home, name='return_home'),

    url(r'^rental$', views.ClientHasBoardGameList.as_view(), name='clienthasboardgame_list'),
    url(r'^rental/new$', views.ClientHasBoardGameCreateView.as_view(), name='clienthasboardgame_create')
]
