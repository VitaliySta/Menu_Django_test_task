from django.db import models


class Menu(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительская категория',
    )
    url = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Ссылка',
    )

    def get_parents(self):
        if self.parent:
            return self.parent.get_parents() + (self.parent.id,)
        return None,

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
