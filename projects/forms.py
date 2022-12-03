from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Project,Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        
        fields = ['title','featured_image','description','demo_link','source_link']
        
        widgets = {
          'tags' : forms.CheckboxSelectMultiple()
        }

        def __ini__(self,*args,**kwargs):
          super(ProjectForm,self).__init__(self,*args,**kwargs)

          for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

          #self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
  

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
          'value':'Placer your vote',
          'body':'Add a comment with your vote'
        }
         
    def __ini__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})         