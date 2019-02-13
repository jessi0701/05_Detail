from django.shortcuts import render

# Create your views here.
def list(request):
    
    return render(request, "detail/list.html")
    
def signup(request):
    return render(request, "detail/signup.html")
    
def mypage(request):
    return render(request, "detail/mypage.html")
    
def qna(request):
    return render(request, "detail/qna.html")

def handler404(request,not_found):
    
    return render(request, "detail/404.html",{"not_found":not_found})
