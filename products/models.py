from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)  # 상품 이름
    description = models.TextField(blank=True)  # 상품 설명
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 상품 가격
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True)  # 수정 날짜
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자 (외래키)

    def __str__(self):
        return self.name