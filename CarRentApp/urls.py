from django.urls import path

from . import views, service

urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:pk>', views.createPost, name='createPost'),
    # path('<int:pk>/', views.car_update_view, name='car_change'),

    path('ajax/load-cars/', views.load_cars, name='ajax_load_model'),  # AJAX

    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('get_model', service.get_json_items_data, name='get_model')
]
