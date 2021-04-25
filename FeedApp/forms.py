from django import forms
from .models import Post, Profile, Relationship

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description','image']
        labels = {'description': 'What would you like to say?'}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','dob','bio']
        labels = {'first_name':'First Name',
                    'last_name':'Last Name',
                    'email':'Email',
                    'dob':'Date of Birth',
                    'bio':'Bio'}

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = '__all__'
        labels = {
            'sender':'Accept friend request from:',
            'receiver':'Send friend request to:',
            'status': 'Current status:'

        }

