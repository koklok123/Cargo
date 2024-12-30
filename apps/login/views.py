from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RegistrationForm
from .models import CustomUser, Profile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Деактивируем до подтверждения email
            user.save()

            # Отправка email с кодом подтверждения
            send_mail(
                'Подтверждение регистрации',
                f'Ваш код подтверждения: {user.confirmation_code}\n'
                f'Или перейдите по ссылке: http://127.0.0.1:8000/confirm-email/{user.confirmation_code}/',
                'your_email@gmail.com',
                [user.email],
                fail_silently=False,
            )
            return render(request, 'login/registration/confirmation_sent.html')
    else:
        form = RegistrationForm()
    return render(request, 'login/registration/register.html', {'form': form})

def confirm_email(request, code):
    try:
        user = CustomUser.objects.get(confirmation_code=code)
        user.is_active = True
        user.is_email_confirmed = True
        user.save()
        return render(request, 'login/registration/confirmation_success.html')
    except CustomUser.DoesNotExist:
        return render(request, 'login/registration/confirmation_failed.html')


@login_required
def profile(request):
    return render(request, 'login/profile.html', {'user': request.user})


def profiles(request):
    profile = Profile.objects.all()
    return render(request, 'profile.html', {'profile_list': profile})