from django.urls import path
from .. import views

user_urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/all/', views.get_users, name='users'),
    path('users/register/', views.register_user, name='user_register'),
    path('users/profile/', views.get_user_profile, name='user-profile'),
    path('users/profile/update/', views.update_user_profile,
         name='user-profile-update'),
]
