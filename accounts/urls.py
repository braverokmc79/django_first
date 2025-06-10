from django.urls import path
from . import views

# # 네임스페이스 지정 하면 템플릿에서 URL을 참조할 때 'accounts:signup'과 같이 사용해야 하므로 불필요
# app_name = "accounts" 

  
urlpatterns = [   
    path('signup/', views.signup, name='signup'),
    
    #기본적으로 제공하는 로그인 폼 사용
    #path('login/', views.login, name='login'),

]


