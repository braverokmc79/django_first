from django.db import models
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        
    #연습용 필드 추가
    #test_fileld=models.CharField(max_length=50, default='임시')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='최근에 게시되었나요?',
    )
    def was_published_recently(self):
        from django.utils import timezone
        import datetime
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            
    def __str__(self):
        return self.question_text
    

    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text =models.CharField(max_length=200)
    votes =models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
        