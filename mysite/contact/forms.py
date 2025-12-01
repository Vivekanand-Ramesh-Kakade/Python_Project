from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    subject = forms.CharField(max_length=150)
    about = forms.CharField(widget=forms.Textarea, label="Tell us about yourself")

    # Basic validation example
    def clean_about(self):
        about = self.cleaned_data['about'].strip()
        if len(about) < 20:
            raise forms.ValidationError("Please provide at least 20 characters.")
        return about
