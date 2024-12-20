from django.urls import path, re_path
#from django.contrib.auth import views as defaultViews
from . import views

app_name = 'djVsanCapacity'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view() , name='index'),
    re_path(r'^Clusters/entry/$', views.ClusterEntry.as_view(), name='cluster-entry'),
    #re_path(r'^update/(?P<pk>[0-9]+)/$' , views.ClusterUpdate.as_view(), name='cluster-update'),
    path('update/<int:pk>/' , views.ClusterUpdate.as_view(), name='cluster-update'),
    re_path(r'^Clusters/(?P<pk>[0-9]+)/delete$' , views.ClusterDelete.as_view(), name='cluster-delete'),
]