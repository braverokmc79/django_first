from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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

