from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters, views
from rest_framework.response import Response
from webapi.models import *
from webapi.serializer import *

# Create your views here.


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# TODO ; 【Django REST framework】POST時はForeignKeyをpkのみ指定し、GET時はネストしたオブジェクトを展開する | https://sakataharumi.hatenablog.jp/entry/2018/10/20/010806


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


# values() 関数を使用して、QuerySet を JSON に変換する
# https://www.delftstack.com/ja/howto/django/django-queryset-to-json/#values-%E9%96%A2%E6%95%B0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6queryset-%E3%82%92-json-%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B
class TechnologyApiView(views.APIView):
    def get(self, request, format=None):
        qs = Technology.objects.all()
        lang = qs.filter(category=1)
        tools = qs.filter(category=2)
        infra = qs.filter(category=3)

        return Response({
            "languageList": lang.values("id", "name"),
            "toolList": tools.values("id", "name"),
            "infraList": infra.values("id", "name"),
        })
