from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

#✅ index 전체 질문중 5개만 조회 (FBA 기반 View)
# index(최신글 list)
def index(request):
	# return HttpResponse("Hello) 기존코드	
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = {"latest_question_list": latest_question_list}
	return render(request, "polls/index.html", context)


#✅ detail : 상세조회
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {"question": question})



#  ✅ results : 결과보기
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


#✅ vote : 투표하기 
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)    
    try:
        selected_choice= question.choice_set.get(pk=request.POST["choice"])        
    except (KeyError, Choice.DoesNotExist):
        # 선택하지 않고 제출한 경우 다시 질문 페이지로
        return render(request, "polls/detail.html", {
		  		"question": question,
			  	 "error_message": "선택을 하지 않았습니다.",
		    })
    else:
      selected_choice.votes += 1
      selected_choice.save()    
      # POST 성공 시 리디렉션
      return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



    # print("== Vote View Called ==")
    # print(f"Question ID: {question_id}")
    # print(f"Request method: {request.method}")
    # print(f"POST data: {request.POST}")  # POST 방식일 경우 폼 데이터 출력












