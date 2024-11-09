from django.urls import path,include
from . import views as drf_app_views
urlpatterns = [
#     path("all-products/",drf_app_views.all_products),
#     path("create-product/",drf_app_views.create_product),
#     path("update-product/<int:id>/",drf_app_views.update_product),
#     path("delete-product/<int:id>/",drf_app_views.delete_product),
    path("colors/",drf_app_views.ColorCreateListUpdateRetrieveDelete.as_view()),
    path("colors/<uuid:id>/",drf_app_views.ColorCreateListUpdateRetrieveDelete.as_view()),
    path("products/",drf_app_views.ProductCreateListUpdateRetrieveDelete.as_view()),
    path("products/<uuid:id>/",drf_app_views.ProductCreateListUpdateRetrieveDelete.as_view())
]

