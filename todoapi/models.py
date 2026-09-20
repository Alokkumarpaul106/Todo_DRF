from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='categories')
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Task(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('rejected','Rejected'),
        ('completed','Completed')
    ]

    PRIORITY_CHOICES=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
        
    ]

    title=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    priority=models.CharField(max_length=20,choices=PRIORITY_CHOICES,default='low')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
