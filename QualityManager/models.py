from django.db import models
from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    """用户表"""
    nick_name=models.CharField(max_length=10,verbose_name="角色",default="默认")
    avit_img=models.CharField(max_length=100,verbose_name="头像路径",null=True)
    def __str__(self):
        return self.username
class Version(models.Model):
    """版本表"""
    version=models.CharField(max_length=16,verbose_name="版本号")
    name=models.CharField(max_length=8,verbose_name="版本名")
    def __str__(self):
        return "%s_%s"%(self.name,self.version)
class Project(models.Model):
    """项目类型"""
    caption=models.CharField(max_length=10,verbose_name="项目类型")
    def __str__(self):
        return self.caption
class BugDetail(models.Model):
    """bug详情表"""
    ver=models.ForeignKey(to="Version",on_delete=models.SET_NULL,null=True,related_name="ver")
    pro=models.ForeignKey(to="Project",on_delete=models.SET_NULL,null=True,related_name="pro")
    title=models.CharField(max_length=32,verbose_name="标题")
    content=models.CharField(max_length=128,verbose_name="内容")
    STATUS_CHOISE=((0,"未解决"),(1,"已解决"),(3,"设计如此"),(4,"延期处理"),(5,"无法重现"))
    status=models.CharField(choices=STATUS_CHOISE,default=0,verbose_name="状态",max_length=8)
    order_to=models.ForeignKey(to="UserInfo",on_delete=models.SET_NULL,null=True)
    creat_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    LEVEL_STATUS=((1,"1"),(2,"2"),(3,"3"),(4,"4"))
    level=models.CharField(choices=LEVEL_STATUS,default=3,verbose_name="bug等级",max_length=8)
    attachment=models.CharField(max_length=100,verbose_name="附件路径",null=True)
    creat_user=models.ForeignKey(to="UserInfo",on_delete=models.SET_NULL,null=True,related_name="creat_user")
    def __str__(self):
        return self.title