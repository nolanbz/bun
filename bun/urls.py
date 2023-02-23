from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from accounts.views import (
    login_view,
    logout_view,
    register_view
)

from .views import home_view

urlpatterns = [
    path('', home_view),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('profile/logout/', logout_view),
    path('register/', register_view),
    path('profile/', TemplateView.as_view(template_name="accounts/profile.html"), name='profile'),
    path('api/', include('api.urls')),
]