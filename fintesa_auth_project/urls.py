"""
URL configuration for fintesa_auth_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from main_app.views import LogoutView 
from main_app import views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.homepage, name='home'),
    
    #  can i use django built-in? such as:
    # path("auth/logout/", LogoutView.as_view(next_page="login"), name="logout"),
    #  path("auth/", include("django.contrib.auth.urls")),

    path('register/', api.RegisterView.as_view() , name='register'),
    path('login/', api.LoginView.as_view() , name='login'),
    path('logout/', api.LogoutView.as_view() , name='logout'),
    path('users/me/', api.MeView.as_view() , name='me'),
    path('admin-only/', api.AdminView.as_view() , name='admin_only/'),

    # ---- extra pathes
    path("try/register/", api.register_form, name="try_register"),
    path("try/login/", api.login_form, name="try_login"),

]
