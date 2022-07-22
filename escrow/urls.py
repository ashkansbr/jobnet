from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/company/', include('company.api.urls')),
    path('api/address/', include('address.api.urls')),
    path('api/accounts/', include('accounts.api.urls'))
]
