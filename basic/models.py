from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Groups(models.Model):
    userName=models.CharField(max_length=100,unique=False,null=True)
    slugGroups=models.SlugField(unique=False,null=True,blank=True)
    groupName=models.CharField(max_length=50,blank=True,unique=False,null=True)
    def __str__(self):
        return self.groupName
    class Meta:
        verbose_name="groupName"


class Base(models.Model):


     class Meta:
        verbose_name="Base Class"

class Titles(models.Model):
    diff_prior_val = (
        (1, 1),
        (2, 2),
        (3, 3),
    )
    given_val=((0,0),(1,1),)

    username=models.CharField(max_length=50,unique=False,null=True,blank=True)
    given = models.IntegerField(choices=given_val,blank=True,default=0 )
    groupname=models.CharField(max_length=50,unique=False,null=True,blank=False)
    title=models.CharField(max_length=50,unique=False)
    difficulty=models.PositiveSmallIntegerField(blank=True,choices=diff_prior_val,default=1)
    priority=models.IntegerField(choices=diff_prior_val,blank=True,default=1 )
    questions=models.CharField(max_length=100,unique=False,null=True,blank=True)
    answer_text=models.TextField(max_length=1000,blank=True,null=True)
    answer_image=models.ImageField(upload_to="answer_as_images",blank=True,null=True)
    unique_key=models.CharField(max_length=100,unique=True,null=True,blank=True)
    no_of_time_accessed=models.PositiveSmallIntegerField(blank=True,default=0)
    date_created=models.CharField(max_length=50,unique=False,null=True,blank=True)
    expiry=models.CharField(max_length=20,unique=False,null=True,blank=True)
    time_last_given=models.CharField(max_length=20,unique=False,null=True,blank=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Title"


class Actions(models.Model):
    updated=models.CharField(max_length=50,null=True,blank=True)#holds the newkey
    old_updated_key=models.CharField(max_length=50,null=True,blank=True)#holds the old key
    inserted=models.CharField(max_length=50,null=True,blank=True)

    deleted=models.CharField(max_length=50,null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    deviceName=models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.username
    class Meta:
        verbose_name="Actions_field"




class MyDevices(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    device_name=models.CharField(max_length=50,null=True,blank=True,unique=False)
    def __str__(self):
        return self.device_name
    class Meta:
        verbose_name="UserDevices"



