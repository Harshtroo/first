from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('register/',views.Register.as_view(),name = "register"),
    path('login/',views.Login.as_view(),name= "login"),
    path('show_data',views.ShowData.as_view(),name="show_data"),
    path('edit/<int:e_id>',views.edit,name="edit"),
    path('delete/<int:e_id>',views.delete,name="delete"),
    path('logout', views.logout_button, name='logout'),
]