from django.db import models


# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField("姓名", max_length=30)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES,)
    number = models.CharField("学号", max_length=10) #unique=True

    class Meta:
        ordering = ["id"]
        verbose_name = "学生"
        verbose_name_plural = "学生"
