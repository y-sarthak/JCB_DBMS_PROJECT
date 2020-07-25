from django.urls import path
from .views import home,employee_form_view,test_form_view,employee_update,Employee_list_view,supplier_view,Supplier_list_view,parts_form_view,parts_view,Parts_list_view

app_name="manufacturing"

urlpatterns = [
     path('home/',home),
     # path('test/',test),
     path('create/',employee_form_view),
     path('sup_create/',test_form_view),
     path('update/<int:id>',employee_update,name="employee_update"),
     path('list/', Employee_list_view),
     path('supview/<int:id>',supplier_view,name="supview"),
     path('suplist/', Supplier_list_view),
     path('part_create/', parts_form_view),
     path('parts_view/<int:id>',parts_view,name="partview"),
     path('parts_list/',Parts_list_view)
]

