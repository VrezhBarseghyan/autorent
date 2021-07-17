from django.urls import path

from . import views, service

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addPost, name='add'),
    # path('<int:pk>', views.createPost, name='createPost'),
    # path('<int:pk>/', views.car_update_view, name='car_change'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('catalogue/<int:pk>', views.posts, name='posts'),
    path('catalogue/<int:pk>/order', views.order, name='order'),

    path('ajax/load-cars/', views.load_cars, name='ajax_load_model'),  # AJAX

    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('user', views.userPage, name='user'),

    path('get_model', service.get_json_items_data, name='get_model')
]
