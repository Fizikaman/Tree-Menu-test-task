from django.db import models


class CategoryMenu(models.Model):
    """Модель категории меню"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TreeMenuBar(models.Model):
    """Модель для древовидного меню"""
    title = models.CharField(max_length=100)
    url = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
