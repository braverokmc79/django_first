from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView

def signup(request):
    if request.method == 'POST':
        # 회원가입 처리 로직
        form =UserCreationForm(request.POST)
        if( form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        # GET 요청 시 회원가입 폼을 보여줌
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})    



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # 커스텀 템플릿 경