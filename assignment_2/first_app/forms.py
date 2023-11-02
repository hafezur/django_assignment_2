from django import forms

from first_app.models import TodoTaskModel
class TodoTaskForm(forms.ModelForm):
    class Meta:
        model=TodoTaskModel
        fields=['id','title','description','status']