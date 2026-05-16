from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from links import views as links_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', links_views.home, name='home'),
    path('about/', links_views.about, name='about'),
    path('register/', links_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', links_views.user_logout, name='logout'),
    path('profile/', links_views.profile, name='profile'),
    path('change-password/', links_views.change_password, name='change_password'),
    path('links/', links_views.links_page, name='links'),
    path('links/<int:pk>/edit/', links_views.edit_link, name='edit_link'),
    path('links/<int:pk>/delete/', links_views.delete_link, name='delete_link'),
    path('s/<str:code>/', links_views.redirect_short, name='redirect_short'),
]