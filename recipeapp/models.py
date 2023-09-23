from django.db import models

# Create your models here.
class Recipe(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name= models.CharField(max_length=120)
    food_recipe = models.TextField()
    foodig1 = models.CharField(max_length=200)
    foodig2 = models.CharField(max_length=200)
    foodig3 = models.CharField(max_length=200)
    foodig4 = models.CharField(max_length=200)
    foodig5 = models.CharField(max_length=200)
    foodig6 = models.CharField(max_length=200)
    foodig7 = models.CharField(max_length=200)
    mov_img1 = models.URLField()
    mov_img2= models.URLField()

    def __str__(self):
        return self.food_name

class Review(models.Model):
    Name= models.CharField(max_length=120)
    Mail= models.EmailField(max_length=100)
    Enter_your_thoughts= models.TextField()
    r= models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
      




