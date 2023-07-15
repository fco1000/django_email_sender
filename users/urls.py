from django.urls import path
from django.views.generic import RedirectView
from .views import (
    userCreationView,
    userLoginView,
    userLogoutView,
    userChangeView,
    showUserView
)

urlpatterns = [
    path('', RedirectView.as_view(url='register/', permanent=False)),
    path('register/',userCreationView,name='register'),
    path('login/',userLoginView.as_view(),name='login'),
    path('logout/',userLogoutView.as_view(),name='logout'),
    path('update_user/',userChangeView.as_view(),name='user_update'),
    path('success/',showUserView,name='home')
]