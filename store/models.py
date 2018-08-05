
from django.db import models

# Create your models here.
from organization.models import LastStore
from users.models import MyUser


class Customer(models.Model):

    state_tuple = (
        (0, u'未到店'),
        (1, u'已到店'),
        (2, u'新单'),
        (3, u'已完成'),
    )

    is_from_web = models.BooleanField(verbose_name="是否由网络客服录入", default=True, editable=False)

    name = models.CharField(max_length=20, verbose_name="姓名", null=True)
    phone = models.CharField(max_length=20, verbose_name="手机号")
    state = models.IntegerField(choices=state_tuple, verbose_name="赴约状态", default=0)
    store = models.ForeignKey(LastStore, verbose_name="门店", related_name='web_staff', on_delete=models.DO_NOTHING, null=True, blank=True)
    web_staff = models.ForeignKey(MyUser, verbose_name="网络客服", related_name='web_staff', on_delete=models.DO_NOTHING, null=True, blank=True)
    sex = models.CharField(max_length=20, verbose_name="性别", default='', blank=True)
    age = models.CharField(max_length=20, verbose_name="年龄", default='', blank=True)
    constellation = models.CharField(max_length=20, verbose_name="星座", default='', blank=True)
    address = models.CharField(max_length=50, verbose_name="住址", default='', blank=True)
    job = models.CharField(max_length=20, verbose_name="职业", default='', blank=True)
    order_time = models.CharField(max_length=50, verbose_name="预约时间", null=True, blank=True)
    ill_place = models.CharField(max_length=50, verbose_name="患病部位", default='', blank=True)
    ill_time = models.CharField(max_length=20, verbose_name="患病时间", default='', blank=True)
    ill_kind = models.CharField(max_length=50, verbose_name="患病种类", default='', blank=True)
    #前台
    front_staff = models.ForeignKey(MyUser, verbose_name="所属前台",  related_name='front_staff',  on_delete=models.DO_NOTHING, null=True, blank=True)
    #美容咨询师
    beauty_consultant = models.ForeignKey(MyUser, verbose_name="分配美容咨询师", related_name='beauty_consultant',  on_delete=models.DO_NOTHING, null=True, blank=True)
    #回访时间
    back_date = models.DateField(verbose_name="回访日期", null=True, blank=True)


    # 新增字段 2018-8-3
    # QQ号码
    qq_num = models.CharField(max_length=20, verbose_name="QQ号码", null=True, blank=True)
    # 预约号
    order_num = models.CharField(max_length=50, verbose_name="预约号", null=True, blank=True)
    # 医院
    hospital = models.CharField(max_length=50, verbose_name="医院", null=True, blank=True)
    # 接待医生
    doctor = models.CharField(max_length=50, verbose_name="接待医生", null=True, blank=True)
    # 登记时间
    register_time = models.CharField(max_length=50, verbose_name="登记时间", null=True, blank=True)



    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "客户信息"
        verbose_name_plural = "客户信息"