from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., Bengaluru, Mumbai, Chennai

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='movies')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)  # e.g., 8.5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['release_date']),
            models.Index(fields=['language']),
            models.Index(fields=['location']),
        ]
        ordering = ['-release_date', 'title']

    def __str__(self):
        return f"{self.title} ({self.language}/{self.location})"
