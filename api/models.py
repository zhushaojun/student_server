from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import JSONField


def image_path(instance, filename):
    # 文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    # return 'user_{0}/{1}'.format(instance.user.id, filename)
    return '{0}/{1}'.format(str(datetime.now())[:10], filename)


def get_default_json():
    return {'语文': 80, '英语': 60}


# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField("姓名", max_length=30)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, )
    number = models.CharField("学号", max_length=10)  # unique=True
    photo = models.ImageField("照片", upload_to=image_path, max_length=256, blank=True)
    courses = JSONField("课程", blank=True, default=get_default_json)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "学生"
        verbose_name_plural = "学生"
