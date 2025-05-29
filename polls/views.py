from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    html = """
        <html>
        <head>
         <link rel="stylesheet" href="/static/polls/reset.css">
         <link rel="stylesheet" href="/static/polls/normalize.css">
        </head>

        <body>
            <h1>안녕하세요.</h1>
            <p>여기는 <strong>설문조사(polls)</strong>사이트의 메인 페이지입니다.</p>
            <p>관리자는 설문을 추가하고, 사용자는 투표할 수 있습니다.</p>
        </body>

        </html> 
    """        
    return HttpResponse(html)



