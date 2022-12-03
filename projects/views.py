from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Tag,Review 
from .forms import ProjectForm,ReviewForm
from django.contrib import messages

from .utils import SearchProjects,PaginateProjects  

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from .umteste import testando,SendEmail 
def projects(request):
    #page = 1
    
    results = 3
    search_query = ''


    #page =request.GET.get('page')
    results = 3
    
    search_query = ''

    if request.GET.get('search_query'):
       search_query,projects = SearchProjects(request)
    else:        
       projects = Project.objects.all()
    

    custom_range,projects = PaginateProjects(request,projects,results)
 
    context = {
        'projects':projects,
        'custom_range':custom_range,
        'search_query':search_query
        }

    return render(request,'projects/projects.html',context)


def project(request,pk):
   projectObj = Project.objects.get(id=pk)
   form = ReviewForm()
    
   #testando(request,projectObj)
   #SendEmail()
    
   if request.method=='POST':
       form = ReviewForm(request.POST)
       review = form.save(commit=False)
       review.project = projectObj
       review.owner = request.user.profile
       review.save()
       
       projectObj.getVoteCount

       messages.success(request,'Your review was successfuly submitted')
       return redirect('project',pk=projectObj.id)

   context = {'project':projectObj,'form':form}           
   return render(request,'projects/single-project.html',context)

@login_required(login_url='login')
def createProject(request):

    profile= request.user.profile
    form = ProjectForm() 
    
    if request.method=="POST":
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        #print(request.POST,'create')
        form= ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False) 
            project.owner=profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            messages.success(request,'Project was created successfully')
            return redirect('projects')   
 
    contex ={'form':form}
    return render(request,'projects/project_form.html',contex)

@login_required(login_url='login')
def updateProject(request,pk):
    profile= request.user.profile
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project) 

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        print('newtags ==>',newtags)
        
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account') 
              
    context ={'form':form,'project':project}
    return render(request,'projects/project_form.html',context)
 

@login_required(login_url='login')
def deleteProject(request,pk):
    profile= request.user.profile
    project = profile.project_set.get(id=pk)
    gReturn = 'account'

    if request.method=="POST":
        print(request.POST,'delete')
        messages.success(request,'Project was deleted successfully')
        project.delete() 
        return redirect('account')   
    contex ={'project':project,'gReturn':gReturn}
    return render(request,'delete_template.html',contex)
