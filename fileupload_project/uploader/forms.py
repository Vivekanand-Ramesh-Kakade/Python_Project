# uploader/forms.py
from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'document']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 100 * 1024 * 1024:  # 100MB
                raise forms.ValidationError("Image size exceeds 100MB limit")
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only PNG/JPG images allowed")
        return image

    def clean_document(self):
        doc = self.cleaned_data.get('document')
        if doc:
            if doc.size > 200 * 1024 * 1024:  # 200MB
                raise forms.ValidationError("File size exceeds 200MB limit")
            if not doc.name.lower().endswith(('.pdf', '.txt')):
                raise forms.ValidationError("Only PDF/TXT files allowed")
        return doc
