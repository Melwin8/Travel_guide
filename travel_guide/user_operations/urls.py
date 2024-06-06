"""
URL configuration for travel_guide project.

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
from . import views
from .views import TranslateAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(), name='user-registration'),
    path('admin-register/', views.SuperuserRegistrationView.as_view(), name='superuser-registration'),
    # path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user-login/', views.UserloginView.as_view(), name='user-token_obtain_pair'),
    path('admin-login/', views.AdminloginView.as_view(), name='admin-token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('user-details/', views.UserDetailsView.as_view(), name='user-details'),
    path('update-user/', views.UpdateUserDetailsView.as_view(), name='update-user-details'),
    
    path('send-otp/', views.PasswordResetOTPSendView.as_view(), name='update-user-details'),
    path('otp-validation/', views.OTPValidationView.as_view(), name='otp-validation'),
    path('change-password/', views.ChangePasswordView.as_view(), name='new-password'),

    path('package-crud/', views.PackageCRUDView.as_view()),
    path('package-crud/<int:pk>/', views.PackageCRUDView.as_view(),),

    path('list-packages/', views.ListPackagesView.as_view(), name='list-packages'),
    path('package-detail/<int:pk>/', views.PackageDetailView.as_view(), name='package-detail-view'),

    path('create-comment/<int:pk>/', views.CreateCommentView.as_view(), name='create-comment'),
    path('list-comments/<int:pk>/', views.ListCommentsView.as_view(), name='list-comments'),
    path('delete-comment/<int:pk>/', views.DeleteCommentView.as_view(), name='delete-comment'),


    path('create-blog/', views.CreateBlogView.as_view(), name='create-blog'),
    path('list-blogs/', views.ListBlogsView.as_view(), name='list-blogs'),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),

    path('list-user-blogs/', views.ListUserBlogsView.as_view(), name='list-user-blogs'),
    path('update-blog/<int:pk>/', views.UpdateBlogView.as_view(), name='update-blog'),
    path('delete-blog/<int:pk>/', views.DeleteBlogView.as_view(), name='delete-blog'),
    
    path('create-review/', views.CreatReviewView.as_view(),),
    path('list-reviews/', views.ListReviewView.as_view(),),
    path('review-detail/<int:pk>/', views.ReviewDetailView.as_view(),),
    
    path('translate/', TranslateAPIView.as_view(), name='translate'),
    

]
