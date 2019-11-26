# blog/models.py
from django.db import models
from django.urls import reverse # new
from django.utils import timezone
from crud.models import Member

DEFAULT_MEMBER = 'default member'
class Post(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text[:50]
    myowner = models.ForeignKey(
    Member,default=Member.DEFAULT_PK,
    on_delete=models.CASCADE
    )

    def get_absolute_url(self): # new
        return reverse('home')

    created     = models.DateTimeField(editable=False,default=timezone.now)
    modified    = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created',]
