from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
                     ('M', 'Male'),
                     ('F', 'Female')
                    )
    LIFE_STYLE = (
                    ('1.2', 'Sedentary'),
                    ('1.375', 'Lightly active'),
                    ('1.55', 'Moderately active'),
                    ('1.725', 'Very active'),
                    ('1.9', 'Extra active')
                )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    lifestyle = models.CharField(max_length=20, choices=LIFE_STYLE)

    def __str__(self):
        return self.gender

class Meal(models.Model):
    FOOD_CHOICES = (
                     ('Breakfast', 'Breakfast'),
                     ('Lunch', 'Lunch'),
                     ('Dinner', 'Dinner')
                    )
    food_time = models.CharField(max_length=50, choices=FOOD_CHOICES)
    food_name = models.CharField(max_length=50)
    food_calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    


    
