from django.urls import path
from . import views


app_name = "details"
handler404 = 'feed.views.handler404'
urlpatterns = [
    path("",views.list),
    path("signup/",views.signup),
    path("mypage/",views.mypage),
    path("qna/",views.qna),
    path("<str:not_found>/",views.handler404),
    ]