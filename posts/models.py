from django.db import models

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=200)  #제목
    content =models.TextField()              #본문
    author = models.CharField(max_length=100) # 작성자 이름
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)      # 수정 시간
    is_published = models.BooleanField(default=True)      # 게시 여부
    
    def __str__(self):
        return self.title
    
    