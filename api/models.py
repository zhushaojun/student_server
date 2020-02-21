from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import JSONField
import random


def image_path(instance, filename):
    # 文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    # return 'user_{0}/{1}'.format(instance.user.id, filename)
    return '{0}/{1}'.format(str(datetime.now())[:10], filename)


random.seed()
course_names = ("语文", "数学", "英语", "自然", "社会", "历史", "地理", "物理", "化学", "生物", "音乐")
def get_default_json():
    result_dict = []
    selected_courses = random.sample(course_names, random.randint(1, len(course_names)))
    random.shuffle(selected_courses)
    for course in selected_courses:
        result_dict.append({
            'id': random.randint(1, 1000),
            '课程': course,
            '分数': random.randint(30, 100)
        })
        # result_dict[course] = random.randint(1, 100)

    return result_dict


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
