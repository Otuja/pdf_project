from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Pdf, Subscriber

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class' : 'w-full py-3 px-5 rounded-xl border border-gray-400 bg-gray-50'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class' : 'w-full py-3 px-5 rounded-xl border border-gray-400 bg-gray-50'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class' : 'w-full py-3 px-5 rounded-xl border border-gray-400 bg-gray-50'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class' : 'w-full py-3 px-5 rounded-xl border border-gray-400 bg-gray-50'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class' : 'w-full py-3 px-5 rounded-xl border border-gray-400 bg-gray-50'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class' : 'w-full py-3 px-5 rounded-xl border border-gray-400 bg-gray-50'
    }))

# adding item by users
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('coursename', 'coursecode', 'upload', 'description', 'institution')

        widgets = {
            'coursename': forms.TextInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'coursecode': forms.TextInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'upload': forms.FileInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'institution': forms.TextInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('coursename', 'coursecode', 'upload', 'description', 'institution')

        widgets = {
            'coursename': forms.TextInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'coursecode': forms.TextInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'upload': forms.FileInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            }),

            'institution': forms.TextInput(attrs={
                'class': 'w-full py-2 px-6 rounded-xl border'
            })
        }


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already subscribed.')
        return email