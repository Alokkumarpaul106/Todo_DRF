
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('todoapi.urls')), #used api
    path('api-auth/', include('rest_framework.urls')), # used for api login logout
    
]
