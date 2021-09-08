
from django.urls import path , include

urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('admins/', include('admins.urls')),
    path('',include('accounts.urls'))
    
]
