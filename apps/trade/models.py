from django.db import models
from django.contrib.auth import get_user_model
from users.models import UserProfile

from goods.models import Goods
User = get_user_model()
# Create your models here.

class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    goods_num = models.IntegerField()