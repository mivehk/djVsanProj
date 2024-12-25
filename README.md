# Django VSAN Capacity Project

This project demonstrates a Django-based web portal, which calculates capacity of your VSAN cluster in raw format or effective after applying storage policy, and results are saved in a DB for further analytical purposes.
https://www.youtube.com/watch?v=rxt4Au31NOY
https://github.com/mivehk/djVsanProj.

---

## **Features**

- Restricted dashboard access using Login and logout functionality.
- Calculation of raw and usable VSAN cluster's capacity.

---

## **Getting Started**

### **1. Install Django, create your project and respectivev applications **
```bash
python3 -m pip install django
django-admin startproject "your-project-name"
cd myproject
python3 manage.py startapp "your-app-name"
```

### **2. Enable the App and verify BASE_DIR variable (e.g., by pathlib library )**
```bash
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth',  # Authentication system 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'djVsanAuth',
    'djVsanCapacity',
]
```

### **3. Include URLs for your project **
```bash
from django.contrib import admin
from django.urls import path , include
from django.views import generic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djVsanAuth/', include('djVsanAuth.urls')),
    path('djVsanCapacity/', include('djVsanCapacity.urls')),
    path('', generic.RedirectView.as_view(url='/djVsanAuth/', permanent=True)), 
]
```

### **4. Create directory structure and custom templates for your auth & vsanCapacity application  **
``` bash
├── README.md
├── djVsanAuth
│   │  . . .
│   ├── templates
│   │   ├── base.html
│   │   └── registration
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── register.html
│ 
├── djVsanCapacity
│   │  . . .
│   ├── templates
│   │   └── djVsanCapacity
│   │       ├── Clusters_form.html
│   │       ├── form-template.html
│   │       └── index.html


update TEMPLATES section of django settings to looks for app specific templates
'APP_DIRS': True,
```

### **5. Add your application's URLs in two separate files and configure their respective views**
```bash
from django.urls import path, re_path
from django.contrib.auth import views as defaultViews
from . import views

app_name = 'djVsanAuth'

urlpatterns = [
    path('', defaultViews.LoginView.as_view(template_name='registration/login.html')),
    path('register/', views.register, name='register'),  
    path('login/', defaultViews.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('logout/', defaultViews.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  
    path('dashboard/', views.dashboard, name='dashboard'), 
]

app_name = 'djVsanCapacity'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view() , name='index'),
    re_path(r'^Clusters/entry/$', views.ClusterEntry.as_view(), name='cluster-entry'),
    #re_path(r'^update/(?P<pk>[0-9]+)/$' , views.ClusterUpdate.as_view(), name='cluster-update'),
    path('update/<int:pk>/' , views.ClusterUpdate.as_view(), name='cluster-update'),
    re_path(r'^Clusters/(?P<pk>[0-9]+)/delete$' , views.ClusterDelete.as_view(), name='cluster-delete'),
]
#look at the class-based views from geenric.edit package & restricted django views for djVsanAuth usign built-in forms 

```

###**6- Include redirection routes in the settings file**
```bash
LOGIN_REDIRECT_URL = '/djAuthApp/dashboard/'
LOGOUT_REDIRECT_URL = '/djAuthApp/login'
LOGIN_URL = '/djAuthApp/login'
```

###**8- Generate migration files and apply them on your local SQLite db**
```bash
python manage.py makemigrations
python manage.py migrate
```

###**9- Run django server if you are deploying application lcoally**
```bash
python manage.py runserver
```

###**10- create superuser (optional)**
```bash
python3 manage.py createsuperuser
Username: admin
Email address: xxxxxx@xxx.com
Password: 
Password (again): 
Superuser created successfully.
```




