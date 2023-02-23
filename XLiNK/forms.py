from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account, Group, Comment
	
from django.utils import timezone


# Create your forms here.

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=True)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields ="__all__"
		widgets = {
			'username': forms.Select(
				attrs={'value': '-id'}
            ),
            'infomation': forms.Textarea(
                attrs={'placeholder': 'ユーザーの自己紹介'}
            ),
			'explain': forms.Textarea(
                attrs={'placeholder': 'ユーザーの基本情報'}
            ),
        }
	def save(self, commit=True):
		user = super(AccountForm, self).save(commit=True)
		user.name = self.cleaned_data['name']
		if commit:
			user.save()
		return user
class ClassCreateForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = "__all__"
		widgets = {
			'manager_name' : forms.TextInput(
				attrs={'placeholder': 'あなたのユーザー名'}
			),
			'name' : forms.TextInput(
				attrs={'placeholder': 'クラス名(dotto is not )'}
			),
			'explain': forms.Textarea(
				attrs={'placeholder': 'クラスの基本的な説明'}
			)
		}
	def save(self,commit=True):
		user = super(ClassCreateForm, self).save(commit=True)
		user.manager_name = self.cleaned_data['manager_name']
		if commit:
			user.save()
		return user
# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Comment
# 		fields = "__all__"
# 		widgets = {
# 			'text':forms.Textarea(
# 				attrs={'placeholder': "what's goning on ?"},				
# 			),
# 		}
# 	def save(self,commit=True):
# 		user = super(CommentForm, self).save(commit=True)
# 		user.manager_name = self.cleaned_data['name']
# 		if commit:
# 			user.save()
# 		return user
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = "__all__"
		widgets = {
			'Destination': forms.BaseFormSet(
			
			),
			'text': forms.Textarea(
				attrs={'placeholder': "What's goning on?"}
			),
		}
	def save(self,commit=True):
		user = super(CommentForm, self).save(commit=True)
		user.name = self.cleaned_data['name']
		if commit:
			user.save()
		return user