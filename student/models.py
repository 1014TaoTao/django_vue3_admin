from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='学生姓名')
    sex = models.CharField(max_length=100, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    class Meta:
        db_table = "tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
