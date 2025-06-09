from django.shortcuts import render, get_object_or_404

from .forms import QuestionForm ,ChoiceForm
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse ,reverse_lazy
from django.views.generic import ListView
from django.db.models import F
from django.views import generic
from django.views.generic.edit import CreateView 


#✅ index 전체 질문중 5개만 조회 (FBA 기반 View)
# index(최신글 list)
# def index(request):
# 	# return HttpResponse("Hello) 기존코드	
# 	latest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	context = {"latest_question_list": latest_question_list}
# 	return render(request, "polls/index.html", context)


# #✅ detail : 상세조회
# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/detail.html", {"question": question})



# #  ✅ results : 결과보기
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


# #✅ vote : 투표하기 
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)    
#     try:
#         selected_choice= question.choice_set.get(pk=request.POST["choice"])        
#     except (KeyError, Choice.DoesNotExist):
#         # 선택하지 않고 제출한 경우 다시 질문 페이지로
#         return render(request, "polls/detail.html", {
# 		  		"question": question,
# 			  	 "error_message": "선택을 하지 않았습니다.",
# 		    })
#     else:
#       selected_choice.votes += 1
#       selected_choice.save()    
#       # POST 성공 시 리디렉션
#       return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



    # print("== Vote View Called ==")
    # print(f"Question ID: {question_id}")
    # print(f"Request method: {request.method}")
    # print(f"POST data: {request.POST}")  # POST 방식일 경우 폼 데이터 출력



# 메인 페이지 (질문 목록)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
# 질문 상세 페이지
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"
 
 
# 결과 페이지
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"
 
 
# 투표 처리 로직
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))





class TestView(ListView):
    template_name = "polls/test.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]







class QuestionListView(ListView):
    model = Question  # 어떤 모델의 데이터를 보여줄지
    template_name = 'polls/question_list.html' 
    # 사용할 템플릿 경로
    
    context_object_name = 'question_list'
    # 템플릿에서 사용할 객체 이름
    
    paginate_by = 10  # 페이지당 항목 수 (선택사항)
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')
    
    
    

class QuestionCreateView(CreateView):
    model = Question
    fields = ['question_text', 'pub_date']  # 폼에서 입력받을 필드
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('polls:index')  # 저장 후 이동할 URL




class QuestionUpdateView(generic.UpdateView):
    model = Question
    form_class = QuestionForm
    #fields = ["question_text", "pub_date"]
    template_name = "polls/question_update.html"
    success_url = reverse_lazy("polls:index")
    
    
class QuestionDeleteView(generic.DeleteView):
    model = Question
    success_url = reverse_lazy("polls:index")   
    
    
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'  # 템플릿에서 사용할 변수명
   



#유저가 질문에 대한 선택지(Choice)를 추가할
class ChoiceCreateView(CreateView):
    model =Choice
    form_class = ChoiceForm
    template_name=  "polls/choice_form.html"
    
    def form_valid(self, form):
        question_id = self.kwargs["question_id"]
        question = get_object_or_404(Question, pk=question_id)
        form.instance.question = question
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy('polls:question_detail', kwargs={'pk': self.kwargs['question_id']})





