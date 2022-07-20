
from django.contrib import admin
from django.urls import path
from user import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     path('create/', views.create),
#     path('edit/<int:id>/', views.edit),
#     path('delete/<int:id>/', views.delete)
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cars_index),
    path('create/object/', views.create_object),
    path('cars/edit/<int:id>/', views.cars_edit),
    path('delete/<int:id>/', views.delete)
]