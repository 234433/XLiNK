from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account, Group, Comment
	
from django.utils import timezone



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
		exclude=['name']
		widgets = {
            'infomation': forms.Textarea(
                attrs={'placeholder': 'ユーザーの自己紹介'}
            ),
			'explain': forms.Textarea(
                attrs={'placeholder': 'ユーザーの基本情報'}
            ),
        }
	# def save(self, commit=True):
	# 	user = super(AccountForm, self).save(commit=True)
	# 	user.name = self.cleaned_data['name']
	# 	if commit:
	# 		user.save()
	# 	return user
	def __init__(self, name=None, destination=None, *args, **kwargs):
		self.name = name
		self.destination = destination
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
		xlink_obj = super().save(commit=False)
		if self.name:
			xlink_obj.name = self.name
			if commit==True:
				xlink_obj.save()
		return xlink_obj
class ClassCreateForm(forms.ModelForm):
	class Meta:
		model = Group
		# fields = "__all__"
		exclude=['manager_name']
		widgets = {
			'name' : forms.TextInput(
				attrs={'placeholder': 'クラス名(dotto is not )'}
			),
			'explain': forms.Textarea(
				attrs={'placeholder': 'クラスの基本的な説明'}
			)
		}
	def __init__(self, manager_name=None, *args, **kwargs):
		self.manager_name = manager_name
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
		xlink_obj = super().save(commit=False)
		if self.manager_name:
			xlink_obj.manager_name = self.manager_name
			if commit==True:
				xlink_obj.save()
		return xlink_obj
	# def save(self,commit=True):
	# 	user = super(ClassCreateForm, self).save(commit=True)
	# 	user.manager_name = self.cleaned_data['manager_name']
	# 	if commit:
	# 		user.save()
	# 	return user
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
		exclude = ["user", "destination"]
		widgets = {
 			'text':forms.Textarea(
 				attrs={
			'placeholder': "what's goning on ?",
			'rows':4, 'cols':15,
			},				
 			),
 		}
	def __init__(self, user=None, destination=None, *args, **kwargs):
		self.user = user
		self.destination = destination
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
		xlink_obj = super().save(commit=False)
		if self.user:
			xlink_obj.user = self.user
			xlink_obj.destination = self.destination
			if commit==True:
				xlink_obj.save()
		return xlink_obj