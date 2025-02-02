from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __sta__(self):
        return self.title