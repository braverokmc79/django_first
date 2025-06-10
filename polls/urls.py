from django.urls import path
from . import views


app_name = "polls"  # 네임스페이스 지정
  
  
urlpatterns = [
    # path('', views.index, name='index'),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("<int:question_id>/results/", views.results, name="results"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
   
   
    path('test', views.TestView.as_view(), name='testView'),
    path("test/questions/", views.test_question_list, name="questions_test"),
 


   # ✅ 슬래시 제거
    path("questions/", views.QuestionListView.as_view(), name="questions"), 
    path("questions/<int:pk>/", views.QuestionDetailView.as_view(), name="question_detail"),
    path("questions/create/", views.QuestionCreateView.as_view(), name="question_create"),
    path("questions/update/<int:pk>/", views.QuestionUpdateView.as_view(), name="question_update"),
    path("questions/delete/<int:pk>/", views.QuestionDeleteView.as_view(), name="question_delete"),
 
   
 
   # 질문 선택등록
   path("questions/<int:question_id>/add_choice/", views.ChoiceCreateView.as_view(), name="choice_create"),
 
 
]


