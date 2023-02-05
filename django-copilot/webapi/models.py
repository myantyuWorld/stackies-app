from django.db import models
from django.contrib.auth import get_user_model

class Member(models.Model):
    name = models.CharField('氏名', max_length=255)
    email = models.CharField('E-Mail', max_length=255)
    age = models.IntegerField('年齢', blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'member'

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Technology(models.Model):
    category = models.ForeignKey(Category, verbose_name="カテゴリID", on_delete=models.CASCADE)
    name = models.CharField('技術名', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'technology'

# TODO : 以下、設計中
# class ExperienceTechnology(models.Model):
#     user_id = models.ForeignKey(get_user_model(), verbose_name="会員ID", on_delete=models.CASCADE)
#     technology = models.ForeignKey(Technology, verbose_name="技術ID", on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'experience_technology'
