from django.db import models

class Category(models.Model):
    name = models.CharField("Category", max_length=255)
    parent = models.ForeignKey("Parent Category",
        'self', on_delete=models.CASCADE, related_name='children', null=True, blank=True
    )
    slug = models.SlugField("URL", max_length=255, unique=True, null=False, editable=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('parent', 'slug')
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    
