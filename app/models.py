from django.db import models

class Resume(models.Model):
    user = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to='resumes')
    feedback = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)