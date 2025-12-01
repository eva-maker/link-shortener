from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from links import views as links_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # прості сторінки
    path('', links_views.home, name='home'),
    path('about/', links_views.about, name='about'),

    # реєстрація / логін / логаут
    path('register/', links_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('logout/', links_views.user_logout, name='logout'),

    # особистий кабінет + посилання
    path('profile/', links_views.profile, name='profile'),
    path('links/', links_views.links_page, name='links'),


    path('s/<str:code>/', links_views.redirect_short, name='redirect_short'),
]
