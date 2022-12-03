from datetime import datetime
 
from django.core.mail import send_mail
from django.conf import settings

def testando(request,project):
   print('===>>>>>>>>>>>>>>>>>>Aki umtest')
   print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
   print('project ==>>',project.title)
   
   

   reviews=project.review_set.filter(project=project)
   
   try:
       print('list(project.reviewers) ==>>>',list(project.reviewers))
   except:
       print('list(project.reviewers) ==>>> ERROR !!!')   

   for review in reviews:
       print('review',review.body)

   if request.user.is_authenticated:
       print('user.is_authenticated')
   else:
       print('user.is_NOT authenticated')       

   try:
    if request.user.profile.id in project.reviewers:
           print('user review finded')

   except:
        print('ERRO ==>>  in project.reviewers:')



def SendEmail():
    
    subject = 'Welcome to DevSearch'
    message = 'We are glad you are here'

    send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['mbarozzi@gmail.com'],
            fail_silently=False,
            )


 