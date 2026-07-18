from django.db import models


class Experience(models.Model):
    job_title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if this is your current position")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.job_title} at {self.company}"

    @property
    def is_current(self):
        return self.end_date is None


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if ongoing")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    @property
    def is_current(self):
        return self.end_date is None
    

class Certificate(models.Model):
    title = models.CharField(max_length=150)
    issuing_organization = models.CharField(max_length=150)
    date_earned = models.DateField()
    credential_url = models.URLField(blank=True, help_text="Link to verify this certificate, if available")
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    class Meta:
        ordering = ['-date_earned']

    def __str__(self):
        return self.title