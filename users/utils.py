from django.db.models import Q
from .models import Profile,Skill

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def PaginateProfiles(request,profiles,results):

   if request.GET.get: 
      page =request.GET.get('page')

   paginator=Paginator(profiles,results)
    
   try:
        profiles = paginator.page(page)
   except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
   except  EmptyPage:   
        page = paginator.num_pages
        profiles = paginator.page(page)
     
    
   leftIndex=(int(page)-4)
   if leftIndex < 1:
        leftIndex=1
    
   rightIndex=(int(page)+5)
   if rightIndex>paginator.num_pages:
       rightIndex=paginator.num_pages+1

   custom_range = range(leftIndex,rightIndex)

   return custom_range,profiles


def SearchProfile(request):
    
     search_query =''
    
     if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
        # por deulft e and
        #profiles = Profile.objects.filter(name__icontains =search_query,short_intro__icontains =search_query,bio__icontains =search_query)
        # | (OR) & (AND)
        # 
        #
        #
     
      
     skills=  Skill.objects.filter(name__icontains =search_query)
 

     profiles = Profile.objects.distinct().filter(Q(name__icontains =search_query) | 
                                            Q(short_intro__icontains =search_query) | 
                                            Q(skill__in = skills)
                                           )
     return search_query,profiles