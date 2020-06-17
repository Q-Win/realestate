from django.urls import path

from . import views
# if we leave the '' empty in the path method below, it will default to this app/model. So in this case it would be root_address + /listings
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
