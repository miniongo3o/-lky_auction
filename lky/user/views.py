from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User # 장고가 주는 User 모델 
from django.contrib import auth
from .models import My_user
from auction.models import Product
from django.contrib import messages
from .models import My_user


def signup(request):
    """회원가입"""
    user_db = User.objects.all()
    if request.method == "POST":
        # 아이디가 존재하면 에러 메세지를 띄워준다.
        if user_db.filter(username=request.POST["username"]).exists():
            print('id error')
            return render(request , 'user/signup.html', {'error':'아이디가 이미 존재합니다.'})
        
        if request.POST["password1"] == request.POST["password2"]: # 비밀번호가 같으면 회원가입
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"],
                email=request.POST["email"]
            )
            my_user=My_user(user=user,credit=0)
        
            my_user.save()
            # 회원가입이 완료 되었습니다, 로그인 해주세요
            # return redirect('/') # 다른 API로 넘어가는것
            return render(request, 'user/login.html', {'success' : '회원가입이 완료되었습니다. \n 로그인 해주세요!!!'})
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')


def login(request):
    """로그인"""
    if request.method == "POST":
        username = request.POST["your_name"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password) 
        if user is not None: # 유저가 존재하면 이전페이지로?
            auth.login(request, user)
            return HttpResponseRedirect('/')
            # return render(request, 'auction/index.html')
        else: # 없으면 로그인 페이지를 렌더
            return render(request, 'user/login.html', {'error':'username or password is incorrect'})
            # 로그인 실패시 'username or password is incorrect' 메시지를 띄움  
    else:
        return render(request, 'user/login.html')


def logout(request):
    """로그아웃"""
    auth.logout(request)
    # 로그아웃되었습니다. 메세지 띄워주기
    return HttpResponseRedirect('/')


def mypage(request):
    """마이페이지"""
    user_id = request.user

    if request.method == "POST":
        new_email = request.POST["email"]
        user_id.email = new_email
        user_id.save()
        return HttpResponseRedirect('/')

    else:
        nowuser = My_user.objects.get(user_id=user_id.id)
        now_product=Product.objects.filter(last_bidder_id=user_id.id)
        context = {'credit' : nowuser.credit, 'now_product':now_product }
        return render(request, 'user/mypage.html', context)