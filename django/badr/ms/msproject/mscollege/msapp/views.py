import email
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .models import CustomUser,Staffs,Students,AdminHOD,SessionYearModel

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")   

def loginUser(request):
    return render(request,"login_page.html")        

def logoutUser(request):
    logout(request)
    return redirect('/')    

def doLogin(request):
 
    print("here")
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    if not (email_id and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'login_page.html')
 
    user = CustomUser.objects.filter(email=email_id, password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'login_page.html')
 
    login(request, user)
 
    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home/')
    elif user.user_type == CustomUser.STAFF:
        return redirect('staff_home/')
    elif user.user_type == CustomUser.HOD:
        return redirect('admin_home/')
 
    return render(request, 'home.html') 



def registration(request):
    return render(request,"registration.html")  

   # Returns CustomUser.user_type corresponding to the given email address
    # email_id should be in following format:
    # '<username>.<staff|student|hod>@<college_domain>'
    # eg.: 'abhishek.staff@jecrc.com'
    

def get_user_type_from_email(email_id):
        try:
            email_id = email_id.split('@')[0]
            email_user_type = email_id.split('.')[1]
            return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
        except:
            return None  
    

def doRegistration(request):
     first_name = request.GET.get("first_name")
     last_name = request.GET.get("last_name")
     email_id = request.GET.get("email")
     password = request.GET.get("password")
     confirmPassword = request.GET.get("confirmPassword")
     
     if not (email_id and password and confirmPassword) :
                        messages.error(request,"Please provide all the details")
                        return render(request,"registration.html")

     if confirmPassword !=  password:
                        messages.error(request,"Confirm pasword not matched with password")
                        return render(request,"registration.html")

     is_user_exists = CustomUser.objects.filter(email=email_id).exists()                   
     
     if is_user_exists:
        messages.error(
            request, 'User with this email id already exists. Please proceed to login!!')
        return render(request, 'registration.html')

     user_type = get_user_type_from_email(email_id)

     if user_type is None:
        messages.error(
            request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
        return render(request, 'registration.html')

     username = email_id.split('@')[0].split('.')[0]   

     if CustomUser.objects.filter(username=username).exists():
        messages.error(
            request, 'User with this username already exists. Please use different username')
        return render(request, 'registration.html')

     user = CustomUser()
     user.username = username
     user.email = email_id
     user.password = password
     user.user_type = user_type
     user.first_name = first_name
     user.last_name = last_name
     user.save()

     if user_type == CustomUser.STAFF:
                     Staffs.objects.create(admin=user)   
     elif user_type == CustomUser.HOD:
                     AdminHOD.objects.create(admin=user)
     elif user_type == CustomUser.STUDENT:
                     Students.objects.create(admin=user)                                        
        

     return render(request,"login_page.html") 

   
   

                    