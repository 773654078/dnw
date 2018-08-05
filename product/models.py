from django.db import models

class productItems(models.Model):
    #产品名
    pName = models.CharField(max_length=30, verbose_name="产品名", null=True)
    #价格
    pprice = models.CharField(max_length=30, verbose_name="价格", null=True)
    #数量
    pnumber = models.IntegerField(verbose_name = '数量')
    def __str__(self):
        return self.pName
    class Meta:
        verbose_name = "产品录入"
        verbose_name_plural = "产品录入"