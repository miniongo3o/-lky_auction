from django.db.models import Q
from django.http import JsonResponse

from .models import Product

import datetime
import json

from datetime import datetime


def index(request):
    category_id = request.GET.get("category")

    if category_id != 'None':
        product = Product.objects.filter(Q(category=category_id) & Q(visible_status='True')).order_by('-pub_date')[:6]
    else:
        product = Product.objects.filter(visible_status='True').order_by('-pub_date')[:6]

    # 경매 마감시 visible_status = False 로 변환
    today = datetime.now()
    for p in product:
        if p.end_date < today:
            p.visible_status = False
            p.save()

    items = list()
    for p in product:
        item = {
            'id': p.id,
            'name': p.name,
            'photo': str(p.photo),
            'thumbnail': p.thumbnail,
            'content': p.content,
            'register': p.register,
            'min_price': p.min_price,
            'max_price': p.max_price,
            'start_date': p.start_date,
            'end_date': p.end_date,
            'pub_date': p.pub_date,
            'category': p.category,
            'visible_status': p.visible_status,
            'last_bidder_id': p.last_bidder_id
        }
        items.append(item)

    context = {
        "result": "successful",
        "product": items
    }
    res = JsonResponse(context, content_type='application/json', status=200, json_dumps_params={'ensure_ascii': False})

    return res

def do_bid(request):
    """입찰 시행"""

    if request.method == 'POST':
        data_dict = json.loads(request.body.decode(encoding='UTF-8'))
        new_item = data_dict['item']
        item = Product.objects.get(id=int(new_item['id']))

        item.max_price = new_item['max_price']
        item.last_bidder_id = new_item['last_bidder_id']
        item.save()

        context = {
            "result": "successful"
        }

        res = JsonResponse(context, content_type='application/json', status=200,
                           json_dumps_params={'ensure_ascii': False})

        return res

    elif request.method == 'GET':
        product_id = request.GET.get("product_id")
        now_max = Product.objects.get(id=int(product_id))
        item = {
            'id': now_max.id,
            'name': now_max.name,
            'photo': str(now_max.photo),
            'thumbnail': now_max.thumbnail,
            'content': now_max.content,
            'register': now_max.register,
            'min_price': now_max.min_price,
            'max_price': now_max.max_price,
            'start_date': now_max.start_date,
            'end_date': now_max.end_date,
            'pub_date': now_max.pub_date,
            'category': now_max.category,
            'visible_status': now_max.visible_status,
            'last_bidder_id': now_max.last_bidder_id
        }

        context = {
            "result": "successful",
            "product": item
        }

        res = JsonResponse(context, content_type='application/json', status=200,
                           json_dumps_params={'ensure_ascii': False})

        return res

    else:
        return JsonResponse({}, content_type='application/json', status=200,
                           json_dumps_params={'ensure_ascii': False})


