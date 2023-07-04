from django.db import models

# Create your models here.
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
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    
    # category (relação)
    
    # author (relação)