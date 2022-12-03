
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

#@receiver(post_save,sender=Profile)
#def profileUpdated(sender,instance,created,**kwargs):
#    print('Profile Saved')                     
#    print('Instance:',instance)
#    print('CREATED:',created)


# usando a notação @receiver(post_save,sender=Profile) não é necessário usar a func abaixo
#post_save.connect(profileUpdated,sender=Profile)

#AKI quando for cadastrado um usuario no django, a tabela Profile sera alinha ou preenchida
#    no evento

#@receiver(post_save,sender=User) 
def createdProfile(sender,instance,created,**kwargs):
    if created:
      user = instance
      print('user Email',user.email)
      profile = Profile.objects.create(
         user = user,
         username=user.username,
         email=user.email,
         name=user.first_name,         
      )
        #MENSAGEM DE BOAS VINDAS
     
      subject = user.first_name +' seja bem vindo ao nosso App DevSearch'
      message = 'Nós estamos felizes por voce '+ user.first_name +' estar aqui'
      
      send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [profile.email],
        fail_silently=False,
        )
      
  

def updateUser(sender,instance,created,**kwargs):
    
    profile = instance
    user = profile.user
    if created==False: 
        user.first_name = profile.name
        user.username = profile.username 
        user.email = profile.email
        user.save() 

def deleteUser(sender,instance,**kwargs):
    try:
       user = instance.user
       user.delete()
    except:
      pass   


post_save.connect(createdProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)