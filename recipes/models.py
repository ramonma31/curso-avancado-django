from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    # EDITED
    # title description slug
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()

    # preparation_time preparation_time_until
    preparation_time = models.IntegerField()
    preparation_time_until = models.CharField(max_length=65)

    # servings servings_until
    servings = models.IntegerField()
    servings_until = models.CharField(max_length=65)

    # preparation_step
    preparation_step = models.TextField()

    # preparation_step_is_html
    preparation_step_is_html = models.BooleanField(default=False)

    # created_at updated_at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # is_published
    is_published = models.BooleanField(default=False)
    
    # cover
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    
    # category (relação)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    
    # author (relação)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
    