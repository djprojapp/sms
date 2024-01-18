from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from PIL import Image

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model= User
        fields = ['first_name', 'last_name']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['institute', 'img']
        labels={
            'img':'Institute Logo',
        }
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['institute'].widget.attrs['placeholder'] = 'Enter School Name'
        self.fields['img'].widget.attrs['placeholder'] = 'Enter School Logo'

    def clean_image(self):
        img = self.cleaned_data.get('img')

        if img:
            # Check image type
            if not img.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError("Only JPG or PNG images are allowed.")

            # Check image size
            max_size_kb = 50
            if img.size > max_size_kb * 1024:
                # Resize image if it exceeds 50KB
                resized_image = Image.open(img)
                resized_image.thumbnail((300, 300))  # Adjust size as needed
                resized_image.save(img.path)

            return img