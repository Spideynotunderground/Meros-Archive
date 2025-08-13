from django.db import models


class Ambassador(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    tg_username = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    
