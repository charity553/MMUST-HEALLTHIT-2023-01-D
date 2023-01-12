
# basic URL Configurations
from django.urls import include, path
from rest_framework import routers
from . import views
# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'person', PersonViewSet)
router.register(r'triage', TriageViewSet)
# specify URL Path for rest_framework
urlpatterns = [
    path('', views.home_view, name='home'),
    path('triage/', views.triage_view, name='triage'),
    path('registration/', views.reg_view, name='registration'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
