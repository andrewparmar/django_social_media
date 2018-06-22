from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def jello_world(request):
    print("Jello World")
    return render(request, 'account/index.html', {'title': 'Jello world'})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
# def user_login(request):
#
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         print("Thiss is a test")
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#
#             print(f'*******{user}')
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated Successfully')
#                 else:
#                     return HttpResponse('Disabled Account')
#             else:
#                 return HttpResponse('Invalid Login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form, 'title': 'merry-xmas'})