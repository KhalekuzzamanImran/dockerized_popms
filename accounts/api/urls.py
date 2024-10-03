from rest_framework_simplejwt.views import (TokenRefreshView, )
from accounts.api.views import CustomTokenObtainPairView, AdminUserListCreateApiView, UserProfileRetrieveUpdateView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/profile/', UserProfileRetrieveUpdateView.as_view(), name='user_profile_get'),
    path('user/list/', AdminUserListCreateApiView.as_view(), name='user_list_get'),
]

