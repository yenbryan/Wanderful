from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from travel_app.forms import ProfileUserCreationForm
from wanderful import settings


def home(request):
    if request.user.is_authenticated():
        return redirect('profile')
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you, {} for signing up for our website!'.format(user.username)
            html_content = '<h2>Thanks, {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


def list_it(request):

    return render(request, 'lists/list_it.html')