from django.urls import include,re_path
from customers import views 
 

urlpatterns = [
    re_path('customers/', views.customer_list),
    re_path('customers/', views.customer_list),
    # re_path(r'^customers/[0-9a-f]{32}', views.customer_detail),
]