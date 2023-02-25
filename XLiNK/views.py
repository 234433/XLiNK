from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  render, redirect
from .forms import RegisterForm, AccountForm, ClassCreateForm, CommentForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Account, User, Group, Comment, Category
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q
from django.urls import reverse
from django.urls import reverse, reverse_lazy
@csrf_exempt
def create_request(request):
	if request.method == "POST":
		form = AccountForm(request.POST)
		if form.is_valid():
			users = form.save()
			if users:
				login(request, users)
				messages.success(request, "Create account successful." )
				return redirect("/index/login/")
		messages.error(request, "Unsuccessful create account. Invalid information.")
	form = AccountForm()
	return render (request=request, template_name="account.html", context={"account_form":form})
@csrf_exempt
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
@csrf_exempt
def register_request(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user=form.save()
			if user is not None:
				login(request, user)
				messages.success(request, "Registration successful." )
				return redirect("/index/create/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
@csrf_exempt
def index(request):
    template = loader.get_template('index.html')
    context = {
        'csrf_token': ''
    }
    return HttpResponse(template.render(context, request))
@csrf_exempt
def accounts(request):
	accounts = Group.objects.order_by('-name')[:100000]
	template=loader.get_template('home.html')
	context={
		'csrf_token': '',
		'accounts': accounts,
	}
	return HttpResponse(template.render(context, request))
def account(request, name):
	account= Group.objects.get(account=name)
	template = loader.get_template('class.html')
	context={
		'account': account,
	}
	return HttpResponse(template.render(context, request))
@csrf_exempt
def homes(request):
	homes =Account.objects.order_by('-name')[:100000]
	template=loader.get_template('home.html', 'class.html')
	context={
		'csrf_token': '',
		'homes': homes,
	}
	return HttpResponse(template.render(context, request))
def home(request,pk):
	home=Account.objects.get(pk=pk)
	template = loader.get_template('profile.html')
	context={
		'home': home,
	}
	return HttpResponse(template.render(context, request))
def managers(request):
	managers = Account.objects.order_by('-manager_name')[:100]
	template = loader.get_template('class.html')
	context={
		'csrf_token': '',
		'managers': managers,
	}
	return HttpResponse(template.render(context, request))
def manager(request, pk):
	manager = Account.objects.get(pk=pk)
	template = loader.get_template('profile.html')
	context = {
		'manager': manager
	}
	return HttpResponse(template.render(context, request))

def communitys(request):
	communitys = Group.objects.order_by('-name')[:10]
	template = loader.get_template('community.html')
	context = {
		'communitys':communitys,
	}
	return HttpResponse(template.render(context, request))

def community(request, name):
	name = Group.objects.get(name=name)
	template  = loader.get_template('class.html')
	context = {
		'community': name,
	}
	return HttpResponse(template.render(context, request))
def class_request(request):
	if request.method == "POST":
		form = ClassCreateForm(request.POST)
		if form.is_valid():
			users = form.save()
			if users is not None:
				login(request, users)
				messages.success(request, "Create class successful." )			
			return redirect("/")
		messages.error(request, "Unsuccessful create class. Invalid information.")
	form = ClassCreateForm()
	return render (request=request, template_name="create.html", context={"create_form":form})
class CreateAccountView(generic.CreateView):
	form_class=AccountForm
	template_name = "account.html"
	success_url="/index/login/"
createaccount = CreateAccountView.as_view()
class CreateClassView(generic.CreateView):
	form_class = ClassCreateForm
	template_name="create.html"
	success_url = '/'
classcreate= CreateClassView.as_view()

def groups(request):
	groups = Group.objects.order_by("_manager_name")[:1000]
	template = loader.get_template("class.html")
	context  = {
		'groups': groups
	}
	return HttpResponse(template.render(context, request))
def group(request, pk):
	group = Group.objects.get(pk=pk)
	template  = loader.get_template('manager.html')
	context = {
		'group': group
	}
	return HttpResponse(template.render(context, request))
class IndexView(ListView):
	model = Group
	template_name = "home.html"
	def get_queryset(self):
		queryset = Group.objects.order_by("-class_name")
		keyword = self.request.GET.get("keyword")
		if keyword:
			queryset = queryset.filter(
				Q(class_name__icontains=keyword) | Q(genre__icontains=keyword)
			)
		return queryset
# class CatagoryView(generic.ListView):
# 	model = Group
# 	paginate_by = 10
# 	template_name = "home.html"
# 	def get_queryset(self):
# 		category = get_object_or_404(Category, pk=self.kwargs['pk'])
# 		queryset = Group.objects.order_by('class_name').filter(category=category)
# 		return queryset
def posts_by_category(request, name):
	category = Category.objects.get(name=name)
	accouunts = Group.objects.filter(category=category)
	return render(request, 'home.html', {'category': category, 'accounts':accouunts})
def comments(request):
    template = loader.get_template('class.html')
    comments = Comment.objects.order_by('created_at')[:10000]
    context = {
        'comments': comments
    }
    return HttpResponse(template.render(context, request))
def comment(request,pk):
    template = loader.get_template('class.html')
    comment = Comment.objects.get(pk=pk)
    context = {
        'comment': comment
    }
    return HttpResponse(template.rebder(context, request))
def commenteds(request):
    template = loader.get_template('class.html')
    comments = Comment.objects.order_by('-created_at')[:10000]
    context = {
        'comments': comments
    }
    return HttpResponse(template.render(context, request))
def commented(request,pk):
    template = loader.get_template('class.html')
    comment = Comment.objects.get(pk=pk)
    context = {
        'comment': comment
    }
    return HttpResponse(template.rebder(context, request))

class CommentCreateView(generic.CreateView):
	template_name = "comment_form.html"
	form_class = CommentForm
	success_url = reverse_lazy("community")
	def get_form_kwargs(self):
		kwgs = super().get_form_kwargs()
		kwgs["user"] = self.request.user
		return kwgs
commentcreate = CommentCreateView.as_view()
# def commentcreate(request):
# 	initial_dict = {
#         'Destination': Group.name,
#         'names': Account.name,
#     }
# 	form = ClassCreateForm(request.POST or None, initial=initial_dict)
# 	return render (request=request, template_name="comment_form.html", context={"comment_form":form})
# def nippoUpdateFormView(request, pk):
#     template_name = "class.html"
#     obj = Group.objects.get(pk=pk),
#     initial_values = {"Destination": obj.name, "names":obj.name}
#     form = NippoFormClass(request.POST or initial_values)
#     ctx = {"form": form}
#     if form.is_valid():
#         name = form.cleaned_data["title"]
#         content = form.cleaned_data["content"]
#         obj.title = title
#         obj.content = content
#         obj.save()
#     return render(request, template_name, ctx)