# _*_ coding: utf-8 _*_

__author__ = 'Awareness'

#独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VproShop.settings')

import django
django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_instace = GoodsCategory()
    lev1_instace.code = lev1_cat['code']
    lev1_instace.name = lev1_cat['name']
    lev1_instace.category_type = 1
    lev1_instace.save()

    for lev2_cat in lev1_cat['sub_categorys']:
        lev2_instace = GoodsCategory()
        lev2_instace.code = lev1_cat['code']
        lev2_instace.name = lev1_cat['name']
        lev2_instace.category_type = 2
        lev2_instace.parent_category = lev1_instace
        lev2_instace.save()

        for lev3_cat in lev2_cat['sub_categorys']:
            lev3_instace = GoodsCategory()
            lev3_instace.code = lev1_cat['code']
            lev3_instace.name = lev1_cat['name']
            lev3_instace.category_type = 3
            lev3_instace.parent_category = lev2_instace
            lev3_instace.save()

