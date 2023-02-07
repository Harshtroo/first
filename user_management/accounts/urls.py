from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView 

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('register/',views.Register.as_view(),name = "register"),
    path('login/',views.Login.as_view(),name= "login"),
    path('show_data/',views.ShowData.as_view(),name="show_data"),
    path('edit/<int:e_id>/',views.Edit.as_view(),name="edit"),
    path('delete/<int:pk>/',views.Delete.as_view(),name="delete"),
    path('logout/', views.Logout.as_view(), name='logout'),
#     path(
#          'login/',
#          views.Login.as_view(
#             # template_name='registration/login.html',
#             success_url = '/home/',
#          ),
#          name='login'
#      ),
]
