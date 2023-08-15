from django.shortcuts import render,redirect

from django.http.response import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from .models import*
from django.contrib import messages


# Create your views here.
def home(request):
    categories=Category.objects.all()
    
    return render(request,'home.html',{'categories':categories})

def rctrhome(request):
    return render(request,'rctrhome.html')    

def jobpost(request):
    return render(request,'jobpost.html')    
@login_required(login_url='rctrlogin')
def newposts(request):
    categories=Category.objects.all()
    if request.method=='POST':
        if request.user.is_authenticated:
            if Usermapping.objects.filter(user=request.user,recruiter=True):
                jcategory=request.POST.get('categor')
                jtitle=request.POST['jobtitle']
                jcompany=request.POST['company']
                jlocation=request.POST['location']
                jdescription=request.POST['jobdescription']
                jtype=request.POST['jobtype']
                jsalary=request.POST['salary']
                jexperience=request.POST['experience']
                jskills=request.POST['skills']
                newpost(category_id=jcategory,jobtitle=jtitle,rctr=request.user,company=jcompany,location=jlocation,jobdescription=jdescription,skill=jskills,experience=jexperience, jobtype=jtype,salary=jsalary).save()
                messages.success(request,'Job added successfully') 
                return redirect(postedjobs)
            else:
              messages.warning('Please login')
       
        else:
           messages.warning('Please login')
       

        
    return render(request,'newpost.html',{'categories':categories})  

def blog(request):
    return render(request,'blog.html')             

def blogsingle(request):
    return render(request,'blogsingle.html') 

def browsejobs(request):
    newposts=newpost.objects.all()   #newposts is a variable to store all objects from model newpost
    context={'Job':newposts}
    return render(request,'browsejobs.html',context)  



def categoryjob(request,pk):
    job=newpost.objects.filter(category=pk)  
    category =Category.objects.get(id=pk)
    context={'job':job,'category':category}
    return render(request,'categoryjob.html',context)  

def candidates(request):
    return render(request,'candidates.html')

  

def contact(request):
    return render(request,'contact.html')   
@login_required(login_url='rctrlogin')
def viewapplicant(request):
     if request.user.is_authenticated:
            
            if Usermapping.objects.filter(user=request.user,recruiter=True):
                # jobposter=newpost.objects.filter(rctr=request.user)
              
                applicants=applyform.objects.filter(job__rctr=request.user)
                
                context={'applicants':applicants}
                return render(request,'viewapplicant.html',context)

               
    

        
        


def applicantdetail(request,pk):
    applicantdetails=applyform.objects.get(id=pk)

    context={'applicantdetails':applicantdetails}
    



    return render(request,'applicantdetail.html',context)   
@login_required(login_url='login')
def apply(request,pk):
    jobdetails=newpost.objects.get(id=pk)  
   
    if request.method=='POST': 

        if request.user.is_authenticated:
            
             name=request.POST['name']
             email=request.POST['email']
             phn=request.POST['phone']
             address=request.POST['address']
             city=request.POST['city']
             state=request.POST['state']
             pin=request.POST['pin']
             skills=request.POST['skills']
             experience=request.POST['experience']
             resume=request.FILES['resume']
             image=request.FILES['image']
           
             applyform(job=jobdetails,user=request.user,name=name,email=email,phn=phn,address=address,city=city,state=state,pin=pin,skill=skills,experience=experience,resume=resume,image=image,).save()
            
             messages.success(request,'successfully submitted') 
        
             return render(request,'home.html')
        else:
           messages.warning('Please login')
       

    return render(request,'apply.html',{'JD':jobdetails})  

def   applicationtstatus(request,pk):
    
    applicant=applyform.objects.get(id=pk)
    applicant.status='Accepted'
    applicant.save()
    return redirect(viewapplicant)

def applicationreject(request,pk):
    
    applicants=applyform.objects.get(id=pk)
    applicants.status='Rejected'
    applicants.save()
    return redirect(viewapplicant)



@login_required(login_url='login')
def userappliedjobs(request):
    if request.user.is_authenticated:
        appliedjob=applyform.objects.filter(user=request.user.id)
        context={'appliedjob':appliedjob}


    
        return render(request,'appliedjobs.html',context)
@login_required(login_url='rctrlogin')
def postedjobs(request):
    if request.user.is_authenticated:
        if Usermapping.objects.filter(user=request.user,recruiter=True):
            postedjob=newpost.objects.filter(rctr=request.user.id)
            context={'postedjob':postedjob}


    
            return render(request,'postedjobs.html',context)         

            
def deletepostedjobs(request,pk):
    if (newpost.objects.filter(id=pk,rctr=request.user)):
        forms=newpost.objects.get(id=pk,rctr=request.user)
        forms.delete()
        return redirect(postedjobs)

        








def deleteappliedjobs(request,pk):
    if(applyform.objects.filter(id=pk,user=request.user)):
        form=applyform.objects.get(id=pk,user=request.user)
        form.delete()

        return redirect(userappliedjobs)







        


def rctr_login(request):
    if request.method=='POST':
        loginname=request.POST['rctrname']
        loginpassword=request.POST['rctrpassword']

        user=auth.authenticate(username=loginname,password=loginpassword)
        if user is not None:
            if Usermapping.objects.filter(user=user,recruiter=True):
                 login(request,user)
                 return redirect(rctrhome)
           
           
            else:
                messages.warning(request,'invalid username or password')
                print('invalid username or password')
                return render(request,'auth/rctrlogin.html')   
    
        else:
                messages.warning(request,'invalid username or password')
                print('invalid user')
                return render(request,'auth/rctrlogin.html') 

    return render(request,'auth/rctrlogin.html') 

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username):
                print('username has already taken')
                return render(request,'auth/signup.html')
            elif User.objects.filter(email=email):
                 print('email  already taken') 
                 return render(request,'auth/signup.html')
            else:
                User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password).save() 
                return redirect(user_login)

        else:
            print('password not matching')
        
            return render(request,'auth/signup.html') 
                  
                

    return render(request,'auth/signup.html')  


def user_login(request):
    if request.method=='POST':
        loginname=request.POST['loginname']
        loginpassword=request.POST['loginpassword']

        user=auth.authenticate(username=loginname,password=loginpassword)
        if user is not None:
             if Usermapping.objects.filter(user=user,recruiter=True):
                 messages.warning(request,'invalid username or password')
             else:
                 login(request,user)
                 messages.warning(request,'login successfully')
                 return redirect(home)
               

           
           
        else:
            messages.warning(request,'invalid username or password')
            return render(request,'auth/login.html')   
    


    return render(request,'auth/login.html') 

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout successfully")
    return redirect('home')    

def rctr_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout successfully")
    return redirect('rctrhome')    

def rctr_register(request):
    if request.method=='POST':
        username=request.POST['rctrusername']
        firstname=request.POST['rctrfirstname']
        lastname=request.POST['rctrlastname']
        email=request.POST['rctremail']
        password=request.POST['rctrpassword']
        confirmpassword=request.POST['rctrconfirmpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username):
                messages.warning('username has already taken')
                return render(request,'auth/rctrsignup.html')
            elif User.objects.filter(email=email):
                 messages.warning('email  already taken') 
                 return render(request,'auth/rctrsignup.html')
            else:
                User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password).save() 
                messages.success(request,"sign up successfully")
                return redirect(rctr_login)

        else:
            messages.warning('password not matching')
        
            return render(request,'auth/rctrsignup.html') 
                  
                

    return render(request,'auth/rctrsignup.html')                           