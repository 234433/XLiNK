from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Connection(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   following = models.ManyToManyField(User, related_name='following', blank=True)
   def __str__(self):
       return self.user

class Account(models.Model):
    HOBBIES ={
        ('読書', '読書'),
        ('ゲーム', 'ゲーム'),
        ('映画', '映画'),
        ('TV', 'TV'),
        ('運動', '運動'),
        ('PC', 'PC'),
        ('VR/AR', 'VR/AR'),
        ('プログラミング', 'プログラミング')
    }
    DETAILS = {
        ('小学生', '小学生'),
        ('中学生', '中学生'),
        ('高校生', '高校生'),
        ('大学生', '大学生'),
        ('社会人', '社会人'),
        ('学校', '学校'),
        ('サイト', 'サイト'),
        ('会社', '会社'),
    }
    name= models.OneToOneField(User,unique=True,null=True , on_delete=models.CASCADE)
    infomation = models.TextField(max_length=180, blank=True, verbose_name="infomation")
    hobby =  models.CharField(max_length=8, choices=HOBBIES)
    detail = models.CharField(max_length=8, choices=DETAILS)
    explain = models.TextField(max_length=180,blank=True, verbose_name="explain")

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Account'
        ordering = ["-name"]

class Group(models.Model):
    GENRE={
        ('運動', '運動'),
        ('音楽', '音楽'),
        ('芸術', '芸術'),
        ('投資', '投資'),
        ('経済', '経済'),
        ('科学', '科学'),
        ('企業', '企業'),
        ('TalkClass', 'TalkClass'),
    }
    # manager_name = models.ForeignKey(Account, null=True,blank=True ,on_delete=models.CASCADE )
    manager_name = models.CharField(max_length=25,blank=True, null=True, verbose_name="管理者名")
    class_name = models.CharField(max_length=23, blank=True, null=True, verbose_name="Class名")
    genre = models.CharField(max_length=9, choices=GENRE)
    backimage = models.ImageField(upload_to='media/', verbose_name="BackImage")
    explain = models.TextField(max_length=180,blank=True, verbose_name="explain")
    def __str__(self):
        return str(self.class_name)
    class Meta:
        verbose_name_plural = 'ClassName'
class Comment(models.Model):
    Destination = models.ForeignKey(Group, null=True,blank=True ,on_delete=models.CASCADE)
    user = models.CharField(max_length=25,blank=True, null=True, verbose_name="ユーザー名")
    comment = models.TextField(max_length=180, blank=True)
    image = models.ImageField(upload_to='image/', verbose_name="Image")
    def __str__(self):
        return str(self.comment)
    class Meta:
        verbose_name_plural = 'Comments'
