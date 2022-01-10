from django.shortcuts import render,redirect
from .models import Projects,Review
from .forms import ProjectForm,RateForm
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
    """
    homepage url
    """
    projects = Projects.objects.all()
    return render(request,'home/index.html',{"projects":projects})
  
def new_project(request):
    """
    function to create a new profile from the Projects model
    Args:
    request: HttpRequest object containing data about this function
    """
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            new_proj = form.save(commit = False)
            new_proj.user = user_profile
            new_proj.save()
        return redirect('homepage:index')  
    else:
        form = ProjectForm()
    return render(request,'projects/new_project.html',{'form':form})    

def projects(request,id):
    project = Projects.objects.get(id = id)
    return render(request,'projects/read_more.html',{"projects":project})
 


@login_required(login_url='login')   
def rate(request,id):
    # reviews = Revieww.objects.get(projects_id = id).all()
    # print
    project = Projects.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('homepage:index')
    else:
        form = RateForm()
    return render(request,"projects/rate.html",{"form":form,"project":project})        





def searchprofile(request):
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        searchResults = Projects.search_projects(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'projects/search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'projects/search.html', {'message': message})
