from django.urls import path
from .views import ProductListCreateView  # ProductCreateAPIView가 아닌 ProductListCreateView
from .views import ProductListCreateView, ProductDetailView
urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),  # 여기도 수정 확인
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
]