# -*- coding:utf-8 -*-
from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def hello(request):
    return HttpResponse("Hello world ! ")

def index(request):
    return render(request, 'index.html')

def ff_key_search(request):
    return_result = {}
    try:
        json_data = json.loads(request.body)
        key = json_data['key']
        hq = unicode.lower(json_data['hq'])
        url_a = "https://cafemaker.wakingsands.com/search?string=" + key + "&indexes=item&language=chs&filters=ItemSearchCategory.ID>=1&columns=ID,Icon,Name,LevelItem,Rarity,ItemSearchCategory.Name,ItemSearchCategory.ID,ItemKind.Name&limit=100&sort_field=LevelItem&sort_order=desc"
        response_a = requests.get(url_a)
        data_a = response_a.json()
        category_a = data_a['Results']
        category = []
        price_list = []

        for c in category_a:
            category.append({
                'id': str(c['ID']),
                'name': c['Name']
            })

        for d in category:
            try:
                url = "https://universalis.app/api/柔风海湾/" + d['id'] + "?hq=" + hq
                response = requests.get(url, timeout=10)
                data = response.json()
                price = data['minPriceHQ']
                if hq == "false":
                    price = data['minPrice']
                price_list.append({
                    'id': d['id'],
                    'name': d['name'],
                    'price': price,
                })
                print {
                    'id': d['id'],
                    'name': d['name'],
                    'price': price,
                }
            except:
                pass

        return_result['message'] = price_list
        return_result['result'] = True
        return JsonResponse(return_result, safe=False)

    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 400
        return_result['detail'] = str(traceback.format_exc())
        return JsonResponse(return_result, safe=False)


def ff_item(request):
    return_result = {}
    try:
        json_data = json.loads(request.body)
        item = json_data['item']
        url = "https://universalis.app/api/柔风海湾/" + item
        response = requests.get(url)
        data = response.json()
    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 400
        return_result['detail'] = str(traceback.format_exc())
        return JsonResponse(return_result, safe=False)

def ff_580(request):
    url_a = "https://cafemaker.wakingsands.com/search?string=古典风格&indexes=item&language=chs&filters=ItemSearchCategory.ID>=1&columns=ID,Icon,Name,LevelItem,Rarity,ItemSearchCategory.Name,ItemSearchCategory.ID,ItemKind.Name&limit=100&sort_field=LevelItem&sort_order=desc"
    response_a = requests.get(url_a)
    data_a = response_a.json()
    category_a = data_a['Results']
    category = []
    price_list = []

    for c in category_a:
        category.append({
            'id': str(c['ID']),
            'name': c['Name']
        })

    for d in category:
        url = "https://universalis.app/api/柔风海湾/" + d['id'] + "?hq=true"
        response = requests.get(url)
        data = response.json()
        price = data['minPriceHQ']
        price_list.append({
            'id': d['id'],
            'name': d['name'],
            'price': price,
        })
        print {
            'id': d['id'],
            'name': d['name'],
            'price': price,
        }

    list = json.dumps(price_list)
    return HttpResponse(list, content_type="application/json; charset=utf-8")


def ff_590(request):
    url_a = "https://cafemaker.wakingsands.com/search?string=条约&indexes=item&language=chs&filters=ItemSearchCategory.ID>=1&columns=ID,Icon,Name,LevelItem,Rarity,ItemSearchCategory.Name,ItemSearchCategory.ID,ItemKind.Name&limit=100&sort_field=LevelItem&sort_order=desc"
    response_a = requests.get(url_a)
    data_a = response_a.json()
    category_a = data_a['Results']
    category = []
    price_list = []

    for c in category_a:
        category.append({
            'id': str(c['ID']),
            'name': c['Name']
        })

    for d in category:
        url = "https://universalis.app/api/柔风海湾/" + d['id'] + "?hq=true"
        response = requests.get(url)
        data = response.json()
        price = data['minPriceHQ']
        price_list.append({
            'id': d['id'],
            'name': d['name'],
            'price': price,
        })
        print {
            'id': d['id'],
            'name': d['name'],
            'price': price,
        }

    list = json.dumps(price_list)
    return HttpResponse(list, content_type="application/json; charset=utf-8")

