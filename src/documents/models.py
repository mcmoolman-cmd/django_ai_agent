from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL  # -> "auth.User"

class Document(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(default="Title")
    content=models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True) #db auto update this fiel to when it's created 
    update_at=models.DateTimeField(auto_now=True) #db auto updates this field when it's updated 

    def save(self, *args, **kwargs):
        if self.active and self.active_at is None:
            self.active_at = timezone.now()
        else:
            self.active_at=None
        super().save(*args,**kwargs)