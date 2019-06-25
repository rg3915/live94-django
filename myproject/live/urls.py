from django.urls import path
from myproject.live import views as v


app_name = 'live'


urlpatterns = [
    path('live/', v.live_list, name='live_list'),
    path('add/', v.LiveCreateView.as_view(), name='live_add'),
    path('json/', v.live_json, name='live_json'),
]
