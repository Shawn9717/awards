from django import forms
from .models import Projects,Review
class ProjectForm(forms.ModelForm):
    """
    Form class to create an html form from the projects model
    """
    class Meta:
        model = Projects
        fields = ['title','description','project_image','project_link']



class RateForm(forms.ModelForm):
    """
    model form to create ratings
    Args:
        forms (model): [class to help in creating the model form]
    """
    class Meta:
        model = Review
        fields = ['text','design','usability','content']
