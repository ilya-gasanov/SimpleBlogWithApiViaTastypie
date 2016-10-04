from django.conf.urls import url
from .views import IndexView, ContactView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),

]
