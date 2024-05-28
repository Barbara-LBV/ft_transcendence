"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.views import *
from website.serializers import *
from django.contrib.auth.views import LogoutView, PasswordChangeView
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('website.urls')),
	#path('users/', user_list, name='user_list'),  
	#path('users/<int:id>/', user_detail, name='user_detail'),
	
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('register', register_view, name='register'),
    path('friends/', friends_view, name='friends'),
	
    path('', base, name='base'),
    path('accueil/', accueil, name='accueil'),
    path('games/', games_view, name='games'),
	path('AI/', AI_view, name='AI'),
    path('pong3D/', pong3D, name='pong3D'),
    path('memory_game/', memory_game, name='memory_game'),
    path('account_settings/', account_settings, name='account_settings'),
    path('logout/', LogoutView.as_view(), name='logout'),
	path('password_change/', PasswordChangeView.as_view(), name='password_change'),
]