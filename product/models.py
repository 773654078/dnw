from django.db import models
from items.models import Step
#产品
class productItems(models.Model):
    #产品名
    pName = models.CharField(max_length=30, verbose_name="产品名", null=True)
    #价格
    pprice = models.CharField(max_length=30, verbose_name="价格", null=True)
    #数量
    pnumber = models.IntegerField(verbose_name = '数量')
    #所属项目
    steps = models.ManyToManyField(Step)
    def __str__(self):
        return self.pName
    class Meta:
        verbose_name = "产品录入"
        verbose_name_plural = "产品录入"
#器械
class Instrument(models.Model):
    #器械名称
    instrument_name = models.CharField(max_length=30, verbose_name="器械名", null=True)
    #所属步骤
    instrument_steps = models.ManyToManyField(Step)