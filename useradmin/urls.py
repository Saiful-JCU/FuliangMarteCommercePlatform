from django.urls import path
from useradmin import views

app_name = "useradmin"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("products", views.products, name="products"),
    path("add_product", views.add_product, name="add_product"),
    path("edit_product<pid>", views.edit_product, name="edit_product"),
    path("delete_products<pid>", views.delete_products, name="delete_products"),
    path("orders", views.orders, name="orders"),
    path("order_detail/<oid>/", views.order_detail, name="order_detail"),
    path("change_order_status<oid>/", views.change_order_status, name="change_order_status"),
    path("shop_page/<str:vid>/", views.shop_page, name="shop_page"),
    path("reviews", views.reviews, name="reviews"),
    path("settings", views.settings, name="settings"),
    path("change_password", views.change_password, name="change_password"),
]