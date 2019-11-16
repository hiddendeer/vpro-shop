from django.views.generic.base import View
from goods.models import Goods
import json
from datetime import datetime

#让datetime类型可以JSON序列化
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date()):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)

class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        from django.forms.models import model_to_dict
        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        from django.http import HttpResponse
        return HttpResponse(json.dumps(json_list, cls=CJsonEncoder), content_type='application/json')
