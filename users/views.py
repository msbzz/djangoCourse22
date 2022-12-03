 
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import CustonUserCreationForm,ProfileForm,SkillForm,MessageForm

from django.contrib import messages
from .models  import Profile,Message
from .utils import SearchProfile,PaginateProfiles  

 

def loginUser(request):
    
    page ='login'
     
    
    if request.user.is_authenticated:
       return redirect('profiles')


    if request.method== 'POST':
       username = request.POST['username']
       password = request.POST['password']
       
       try:
         user= User.objects.get(username=username) 
         
       except:
           messages.error(request,'user not exist') 

       user = authenticate(request,username=username,password=password) 
       
       if user is not None:
          login(request,user)
          print('USER ID ==>> ',request.user.id)
          return redirect(request.GET['next'] if 'next' in request.GET else 'account')
          #messages.success( request,'welcome '+user.first_name)
          #return redirect('profiles')
       else:
           messages.error(request,'username OR password is incorrect')  

    #context = {}
    return render(request,'users/login-register.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'you are logout')
    return redirect('login')


def registerUser(request):
    page ='register'
    form = CustonUserCreationForm()

    if request.method=="POST":
        form = CustonUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User account was created')

            login(request,user)
            return redirect('edit-account')
        else:

            messages.error(request,'An error occurred, your account cannot be created during registration')


    context={'page': page,'form':form}
    return render(request,'users/login-register.html',context)


def profiles(request):

    search_query=''
    results =3
     
 
    if request.GET.get('search_query'):
       search_query,profiles = SearchProfile(request)
    else:
       profiles = Profile.objects.all()  

     
    custom_range,profiles = PaginateProfiles(request,profiles,results)
   
   
    context = {'profiles':profiles,'search_query':search_query,'custom_range':custom_range}
    return render(request,'users/profiles.html',context)  
 
def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile':profile,"topSkills":topSkills,
	"otherSkills":otherSkills}
    return render(request,'users/user-profile.html',context) 
 
@login_required(login_url='login') 
def userAccount(request):
    profile =request.user.profile
    context = {'profile': profile}
    return render(request,'users/account.html',context)

@login_required(login_url='login') 
def editAccount(request):

    profile = request.user.profile
    form = ProfileForm(instance=profile)
    print('AKI EDIT-ACCOUNT')

    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
               form.save()
               return redirect('account')
           
    context = {'form': form}
    return render(request,'users/profile_form.html',context)    
 
@login_required(login_url='login')
def createSkill(request):

    profile= request.user.profile
    form = SkillForm() 
    
    if request.method=="POST":
 
        form= SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False) 
            skill.owner=profile
            skill.save()
            messages.success(request,'Skill was added successfully')
            return redirect('account')   
    contex ={'form':form}
    return render(request,'users/skill_form.html',contex)


@login_required(login_url='login')
def editSkill(request,pk):

    profile= request.user.profile
    skill= profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill) 
    
    if request.method=="POST":
 
        form= SkillForm(request.POST,instance=skill)
        if form.is_valid():
            skill.save()
            messages.success(request,'Skill was edited successfully')
            return redirect('account')   
    context ={'form':form}
    return render(request,'users/skill_form.html',context)


@login_required(login_url='login')
def deleteSkill(request,pk):

    profile= request.user.profile
    skill= profile.skill_set.get(id=pk)
    gReturn = 'account'
    
    if request.method=="POST": 
            skill.delete()
            messages.success(request,'Skill was deleted successfully')
            return redirect('account')  
              

    context ={'objectForm':skill,'gReturn':gReturn }
    return render(request,'delete_template.html',context)
 

@login_required(login_url='login') 
def inbox(request):
    profile= request.user.profile
    #messageRequests = profile.message_get.all()
    messageRequests = profile.messages.all()

    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messages':messageRequests,'unreadCount': unreadCount}
    return render(request,'users/inbox.html',context)    

@login_required(login_url='login')
def viewMessage(request,pk):

    
    profile= request.user.profile
    message = profile.messages.get(id=pk)

    if message.is_read == False:
       message.is_read = True
       message.save()

    context = {'message':message}
    return render(request,'users/message.html',context)

def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm() 

    try:
        sender = request.user.profile
    except:
        sender = None 


    if request.method=="POST":
     
        form= MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False) 
            message.sender = sender
            message.recipient = recipient

            if sender:
               message.name = sender.name
               message.email = sender.email

            message.save()

            messages.success(request,'Your message was successfully sent')
            return redirect('user-profile', recipient.id)             
   
    contex ={'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',contex)    