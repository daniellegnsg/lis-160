from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('book/<int:pk>', views.about_book, name='book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:pk>', views.update_book, name='update_book'),

]