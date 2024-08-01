from django.urls import path
from django.urls import path
from .views import home  # home 뷰를 임포트합니다.

urlpatterns = [
    path('', home, name='home'),  # 기본 URL 패턴 추가
]

