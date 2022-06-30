from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<str:name>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('user/', include("django.contrib.auth.urls")),
    path('login/', views.login_request, name='login_request'),
    path('add', views.add, name='add'),
    path('edit', views.edit_profile, name='edit_profile'),
    path('delete/<str:game>', views.delete, name='delete'),
    path('logout', views.logout_request, name='logout_request')
]
