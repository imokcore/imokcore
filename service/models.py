from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=30)
    button_id = models.CharField(max_length=100, blank=True)
    should_be_contacted = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            send_mail('Welcome to Healthy Living', 'Dear {}, Welcome to Healthy Living!'.format(self.name),
                      'imokcore@gmail.com', [self.email], fail_silently=False)

        super(Member, self).save(*args, **kwargs)
