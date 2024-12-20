#from django.shortcuts import render
from .models import Clusters

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#from django.http import HttpResponse


class IndexView(generic.ListView):
	context_object_name='cluster_list'
	template_name = 'djVsanCapacity/index.html'
	#template_name = 'index.html'

	def get_queryset(self):
		return Clusters.objects.filter(user=self.request.user)
		#return Clusters.objects.all()


class ClusterEntry(CreateView):
    model = Clusters
    fields=['CustomerName','OndiskOver','NumDG','NumCapDisks','SSDSize','NumNodes','FTM','Clusterid','RawCap','SpbmCap','user']

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign logged-in user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'ClusterEntry'
        return context
   
class ClusterUpdate(UpdateView):
	model = Clusters
	fields=['CustomerName','OndiskOver','NumDG','NumCapDisks','SSDSize','NumNodes','FTM','Clusterid','RawCap','SpbmCap','user']
	
	def get_object(self, queryset=None):
		return Clusters.objects.get(pk=self.kwargs['pk'])

	def get_queryset(self):
		query= Clusters.objects.filter(user=self.request.user)
		print("retrieved: ", query)
		if not query.exists():
			print("Record not found")
		#print(query)	
		return query

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['view_type'] = 'ClusterUpdate' #adding additional context to the template for debugging
		#print("Form instance data ", self.object)
		'''print("Form instance initial data: ")
		for field_name in self.fields:
		    value = getattr(self.object, field_name, None)
		    print(f"{field_name}: {value}")'''	
		return context

class ClusterDelete(DeleteView):
	model = Clusters
	success_url = reverse_lazy('djVsanCapacity:index')
	
	def get_queryset(self):
		return Clusters.objects.filter(user=self.request.user)
