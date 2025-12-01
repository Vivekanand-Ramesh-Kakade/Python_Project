from django.db import models

def validate_file_size(value):
    filesize = value.size
    if filesize > 200 * 1024 * 1024:  # 200MB
        raise ValidationError("File size exceeds limit")

class Upload(models.Model):
    image = models.ImageField(
        upload_to="uploads/images/",
        blank=True,
        null=True,
        validators=[validate_file_size]
    )
    document = models.FileField(
        upload_to="uploads/docs/",
        blank=True,
        null=True,
        validators=[validate_file_size]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload {self.id}"
