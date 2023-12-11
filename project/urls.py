"""
URL configuration for project project.

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
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/<int:user_id>/<str:token>', VerifyEmailView.as_view(), name='verify'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('verificationsuccess/', VerificationSuccess.as_view(), name='verificationsuccess'),
    path('verificationerror/', VerificationError.as_view(), name='verificationerror'),
    #path('user_list/', UserListView.as_view(), name='user_list'),
    #path('category_list', CategoryListView.as_view(), name='category_list'),
    #path('category_create/', CreateCategoryView.as_view(), name='category_create'),
    #path('category_about/<int:pk>/', DetailCategoryView.as_view(), name='category_about'),
    path('', PostListView.as_view(), name='post_list'),
    #path('post_create/', CreatePostView.as_view(), name='post_create'),
    path('post_update/<int:pk>/', UpdatePostView.as_view(), name='post_update'),
    path('post_about/<int:pk>/', DetailPostView.as_view(), name='post_about'),
    path('post_delete/<int:pk>/', DeletePostView.as_view(), name='post_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)