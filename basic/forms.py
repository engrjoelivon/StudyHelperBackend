from django import forms
from django.contrib.auth.models import User
from basic.models import Titles,Groups

class Userinfo(forms.ModelForm):
    class Meta:
        model=User
        fields=("username","password","email")






class Groupform(forms.ModelForm):
    class Meta:
        model=Groups
        fields=("groupName",)




class Titlesform(forms.ModelForm):

    class Meta:
        model=Titles
        fields=("title","difficulty","priority","answer_text",
                "groupname","questions","id")


