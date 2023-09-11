from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocationAPIView.as_view()),
    path('products/<int:id>/', views.LocationAPIView.as_view()),
    path('<int:location_id>/department/', views.DepartmentAPIView.as_view()),
    path('<int:location_id>/department/<int:department_id>/category/', views.CategoryAPIView.as_view()),
    path('<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/', views.SubCategoryAPIView.as_view()),
    path('<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/<int:subcategory_id>/', views.SubCategoryAPIView.as_view()),
    path('skudata/', views.SKUDataAPIView.as_view()),
]
