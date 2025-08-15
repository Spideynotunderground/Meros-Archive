from django.db import models


class Ambassador(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    tg_username = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    

class Story(models.Model):
    headline = models.CharField(max_length=255, null=True)
    description_en = models.TextField(null=True)
    description_uz = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    

    def __str__(self):
        return self.headline
    

class StoryImage(models.Model):  # 👈 Inherit from models.Model
    story = models.ForeignKey(Story, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"Image for {self.story.headline}"

