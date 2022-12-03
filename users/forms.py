from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from .models import Profile,Skill,Message

class CustonUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ['first_name','email','username','password1','password2'] 

        labels = {
            'first_name':'Name',
            'email':'e-mail',
            'username':'username',
            'password1':'password',
            'password2':'password',
            }

        def __ini__(self,*args,**kwargs):
            super(CustonUserCreationForm,self).__init__(self,*args,**kwargs)

            for name,field in self.fields.items():
               field.widget.attrs.update({'class':'input'})
  

class ProfileForm(ModelForm):
   class Meta:
      model = Profile
      #fields = '__all__'
      fields = [
          'name',
          'username',
          'location',
          'email',
          'short_intro',
          'bio',
          'profile_image',
          'social_twitter',
          'social_stackoverflow',
          'social_linkedin',
          'social_youtube',
          'social_website'
          ]

    
      def __ini__(self,*args,**kwargs):
         super(ProfileForm,self).__init__(*args,**kwargs)

         for name,field in self.fields.items():
               field.widget.attrs.update({'class':'input'})  


class SkillForm(ModelForm):
       class Meta:
         model = Skill
         fields = [
          'name',
          'description',
 
          ]

    
         def __ini__(self,*args,**kwargs):
            super(SkillForm,self).__init__(*args,**kwargs)

            for name,field in self.fields.items():
               field.widget.attrs.update({'class':'input'})                      


class MessageForm(ModelForm):
       class Meta:
         model = Message
         fields = [
          'name',
          'email',
          'subject',
          'body'
           ]

    
         def __ini__(self,*args,**kwargs):
            super(MessageForm,self).__init__(*args,**kwargs)

            for name,field in self.fields.items():
               field.widget.attrs.update({'class':'input'})                      