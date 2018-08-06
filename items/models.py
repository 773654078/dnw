from django.db import models

#项目表
class Item(models.Model):
    #项目名
    item_name = models.CharField(max_length=30, verbose_name="项目名", null=True)
    #价格
    item_price = models.IntegerField(verbose_name = '价格', null=True)
    #次数
    frequency = models.IntegerField(verbose_name = '价格', null=True)
    def __str__(self):
        return self.item_name
#步骤
class Step(models.Model):
    #步骤内容
    step_content = models.CharField(max_length=1000, null=True)
    #所属项目
    belong_item = models.ForeignKey(Item, verbose_name="所属项目", on_delete=models.DO_NOTHING, null=True)


