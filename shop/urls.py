from django.urls import path
from . import views 
urlpatterns = [
	path('', views.productlist, name='productlist' ),
	path('<id>/<slug>', views.productdetail, name="productdetail"),
	path('<category_slug>', views.productlist, name = 'product_list_by_category'),  
]