from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, UpdateUserForm, ShortLinkForm
from .models import ShortLink


# 1) Головна
def home(request):
    return render(request, 'home.html')


# 1) Сторінка "Про нас"
def about(request):
    return render(request, 'about.html')


# 2) Реєстрація
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("profile")
        else:
            error = "Неверное имя пользователя или пароль"

    return render(request, "login.html", {"error": error})


def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


# 4) Особистий кабінет + оновлення даних
@login_required
def profile(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'profile.html', {
        'form': form,
    })


# 5–6) Сторінка з посиланнями
@login_required
def links_page(request):
    user_links = ShortLink.objects.filter(user=request.user).order_by('-created_at')

    if request.method == "POST":
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            short_link = form.save(commit=False)
            short_link.user = request.user
            short_link.save()
            return redirect('links')
    else:
        form = ShortLinkForm()

    return render(request, 'links.html', {
        'form': form,
        'links': user_links,
    })


# 7) Редірект по короткому коду
def redirect_short(request, code: str):
    link = get_object_or_404(ShortLink, short_code=code)
    return redirect(link.original_url)
