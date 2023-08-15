from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=30,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.categoryname




class newpost(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    jobtitle=models.CharField(max_length=30,null=True)
    company=models.CharField(max_length=30,null=True)
    salary=models.IntegerField(null=True)
    rctr=models.ForeignKey(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=30,null=True)
    jobdescription=models.TextField(max_length=500,null=True)
    skill=models.TextField(max_length=500,null=True)
    experience=models.TextField(max_length=500,null=True)
    jobtype=models.CharField(max_length=30,null=True)
    created_at = models.DateTimeField(auto_now_add=True)



class applyform(models.Model):
    job=models.ForeignKey(newpost,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True)
    status=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
    phn=models.IntegerField(null=True)
    skill=models.TextField(max_length=500,null=True)
    experience=models.TextField(max_length=500,null=True)
    address=models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=40)
    city=models.CharField(max_length=20,null=True)
    state=models.CharField(max_length=20,null=True)
    pin=models.IntegerField(null=True)
    resume=models.FileField(null=True)
    image=models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)







class Usermapping(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recruiter=models.BooleanField(default=False)

    def __str__(self):

        return str(self.user)










    

class appliedjobs(models.Model):  
    job=models.ForeignKey(newpost,on_delete=models.CASCADE)
    application=models.ForeignKey(applyform,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)