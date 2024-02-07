from django.db import models

from utils import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='media/', verbose_name='превью', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}.'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='media/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.CharField(max_length=500, verbose_name='ссылка', **NULLABLE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.name}.'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


