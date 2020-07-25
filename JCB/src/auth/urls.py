from django.urls import path
from .views import auth_login_employees,auth_login_supplies,auth_login_parts,logout_view

app_name="auth"

urlpatterns = [
     path('login_manufacturing_employees/',auth_login_employees),
     path('login_manufacturing_supplies/',auth_login_supplies),
     path('login_manufacturing_parts/',auth_login_parts),
     path('logout/',logout_view)
]

