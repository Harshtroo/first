from django import forms
from .models import User
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.forms import UserCreationForm

choice_gender = (
    ("gender","gender"),
    ("male","male"),
    ("female","female")
)
class RegistrationForm(forms.ModelForm):
    '''custom register'''
    gender = forms.ChoiceField(choices= choice_gender)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        '''registr meta'''
        model = User
        fields = ['username','first_name','last_name','email','gender', 'password1','password2']

    def clean(self):
        '''password1 and password2 both are same or nnot '''
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 !=password2:
            raise forms.ValidationError("password don't match.")
        return self.cleaned_data

    def save(self,*args, **kwargs):
        self.instance.password = make_password(self.cleaned_data['password1'])
        super().save(*args,**kwargs)

class LoginForm(forms.ModelForm):
    '''login form '''
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        '''login form meta class'''
        model = User
        fields = ['username','password']

class UpdateForm(forms.ModelForm):
    '''update form '''
    class Meta:
        '''update form meta'''
        model = User
        fields = ['username','first_name','last_name','email','gender']

class DeleteForm(forms.ModelForm):
    ''' delete form in form.py '''
    class Meta:
        '''' delete meta'''
        model = User
        fields = ['username','first_name','last_name','email','gender']
