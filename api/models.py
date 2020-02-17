from django.db import models


# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField("姓名", max_length=30, blank=True, default='-')
    gender = models.CharField("性别", max_length=1, blank=True, default='-', choices=GENDER_CHOICES,)
    student_id = models.CharField("学号", max_length=10, blank=True, default='-') #unique=True

    class Meta:
        ordering = ["student_id"]
        verbose_name = "学生"
        verbose_name_plural = "学生"
