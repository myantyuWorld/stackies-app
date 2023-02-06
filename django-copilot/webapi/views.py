from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
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
