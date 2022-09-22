from django.contrib import admin
from django.urls import path
from inventarioApp.login import login
from inventarioApp.views.customers.create import create_customers
from inventarioApp.views.users.create import create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('customer/create', create_customers),
    path('user/create', create_user)
]
