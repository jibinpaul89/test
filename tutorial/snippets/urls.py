from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.getsnippets, name='snippets'),
    #path('api-auth/', include('rest_framework.urls'))
    path('query/', views.query_view),
]