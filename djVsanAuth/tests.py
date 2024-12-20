import os
import sys
from pathlib import Path
import django
#from django.test import TestCase
#from djVsanCapacity.models import Clusters
from django.forms.models import model_to_dict

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))  #adding /Users/kmive/Desktop/python/new-django-project/djVsanProj/

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djVsanProj.settings')  # now settings is reachable from inside djVsanProj 
django.setup()

from djVsanCapacity.models import Clusters 


c1 = Clusters.objects.get(Clusterid=20)
print(c1)
print(model_to_dict(c1))

# Create your tests here.
