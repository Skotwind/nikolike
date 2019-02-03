from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Photo(models.Model):
    class Meta():
        db_table = "Photo"

    Photo_img = models.ImageField(upload_to='photos', blank=True)
    Photo_name = models.CharField(max_length = 200)
    Photo_about = models.TextField()
    Photo_date = models.DateTimeField(auto_now_add = True)
    Photo_likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.Photo_name

class CommentPhoto(models.Model):

    class Meta():
        db_table = "CommentPhoto"

    Comment_text = models.TextField(verbose_name="Комментарий")
    Comment_date = models.DateTimeField(auto_now_add=True)
    Comment_likes = models.IntegerField(default=0)
    Comment_Photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    Comment_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.Comment_text

class UserAcc(models.Model):

    class Meta():
        db_table = "UserAcc"

    User_name = models.CharField(max_length=200)
    User_age = models.IntegerField()

    def __str__(self):
        return self.User_name

class Cake(models.Model):
    class Meta():
        db_table = "Cake"

    Cake_name = models.TextField(max_length=200)
    Cake_weight = models.IntegerField(default=1)
    Cake_calories = models.IntegerField()
    Cake_type = models.TextField(max_length=200)
    Cake_rating = models.IntegerField(default=5)
    Cake_composition = models.TextField(max_length=2000)

    def __str__(self):
        return self.Cake_name
