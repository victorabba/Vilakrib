from django.db import models
from vialpi.models import User
import datetime

class Jwt(models.Model):
    user=models.OneToOneField(User,related_name='login_user',on_delete=models.CASCADE)
    access=models.TextField()
    refresh=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


