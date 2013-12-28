from datetime import timedelta

from django.utils import timezone
from django.db import models

from lockdown import settings

class TempUnlock(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        self.expires = timezone.now() + timedelta(minutes=settings.TEMP_UNLOCK_MINUTES)
        super(TempUnlock, self).save(*args, **kwargs)
