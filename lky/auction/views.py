from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User

from .forms import registerForm
from .models import Product

from user.models import My_user
from PIL import Image

import uuid
import datetime

from datetime import datetime

def index(request):
    category_id = request.POST.get("products")
    if category_id is not None:
        product = Product.objects.filter(category=category_id).order_by('-pub_date')[:6]
    else:
        product = Product.objects.all().order_by('-pub_date')[:6]

    user_id=request.user
    # credit=My_user.objects.get(user_id=user_id.id)

    # return render(request, 'auction/index.html', {'product': product, 'credit':credit})
    return render(request, 'auction/index.html', {'product': product})


def auctionRegister(request):
    if request.method == 'POST':
        file_data = request.FILES
        file_name = file_data['photo'].name
        idx = list(file_name).index('.')
        f_type_list = list(file_name)[idx:]
        f_type = ''.join(f_type_list)
        data_name = str(datetime.now())[:10] + '-' + str(uuid.uuid1()) + f_type

        file_data['photo'].name = data_name
        form = registerForm(request.POST, request.FILES)

        if form.is_valid():
            prod = form.save(commit=False)
            thumbnail_name = 'thumbnail-' + data_name
            prod.thumbnail = thumbnail_name
            prod.save()
            img = Image.open(settings.MEDIA_ROOT + data_name)
            img_resize = img.resize((int(img.width / (img.height / 240)), 240))
            img_resize.save(settings.MEDIA_ROOT + thumbnail_name)

            return redirect('index')
    else:
        form = registerForm()

    return render(request, 'auction/auction_register.html', {'form': form})

# 홈 상단 바 - 크레딧 충전 클릭
def auction_credit(request):
    return render(request,'auction/auction_credit.html')

# auction_credit.html에서 실행할 충전 함수
# 현재 로그인 중인 auth_user의 id에 해당하는 크레딧을 50000원 증가시킨다.
def charging(request):
    user_id=request.user

    now_credit=My_user.objects.get(user_id=user_id.id)
    now_credit.credit=int(now_credit.credit)+50000
    now_credit.save()
    return render(request,'auction/auction_credit.html')


# def showProductList(request):
#     product = Product
#     return render(request, product)

def do_bid(request):
    if request.POST:
        # attr 없으면 에러뜨게 함. 때문에 형식을 지키지 않은 POST는 막힘.
        input_price = int(request.POST['bid-value'])
        min_price = int(request.POST['product-min'])
        max_price = int(request.POST['product-max'])
        product_id=request.POST['product-id']
        now_max = Product.objects.get(id=product_id)

        user_id = request.user
        now_credit = My_user.objects.get(user_id=user_id.id)
        if input_price>min_price and input_price>max_price and now_credit.credit>input_price:
            now_max.max_price = input_price
            now_max.save()
            now_credit.credit =int(now_credit.credit)-input_price
            now_credit.save()
            print(min_price,max_price,input_price,now_credit)
        return redirect('/')
    else:
        return redirect('/')


