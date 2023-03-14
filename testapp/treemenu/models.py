from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ('parent__create_date', 'create_date')

    def __str__(self) -> str:
        return self.title

    def get_children(self):
        return self.children.all()
