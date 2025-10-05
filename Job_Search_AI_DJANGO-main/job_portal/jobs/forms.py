# jobs/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel, JobModel,FeedModel,CommentModel

from django import forms
from .models import JobPost

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']  # add more fields if needed

class JobForm(forms.ModelForm):

    class Meta:
        model = JobModel
        fields = '__all__'

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'

class FeedForm(forms.ModelForm):
    class Meta:
        model = FeedModel
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['Image', 'date']
    

