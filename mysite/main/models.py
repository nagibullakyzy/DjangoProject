from django.conf import settings
from django.db import models
from django.utils import timezone


class Food(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.food_name

class Comment(models.Model):
    comment = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    comment_text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author

class User(models.Model):
    login = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    #user_dob = models.DateTimeField('date of birth')
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name + " " + self.user_surname

    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.password

    def __str__(self):
        return self.login