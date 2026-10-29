from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
# Create your views here.
def login(request): 
    if request.method=="POST":   
        email=request.POST.get("email")
        otp=str(random.randint(1000,9999))
        request.session["email"]=email
        request.session["otp"]=otp
        send_mail(
            "Your Otp Code",
            f"Your otp is:{otp}",
            "manipulimi2@gmail.com",
            [email],
            fail_silently=False
        )
        if request.method=="POST":
            return redirect("verify_otp")
    return render(request,'app/home.html')
def verify_otp(request):
    if request.method=="POST":
        user_otp=request.POST.get("user_otp")
        otp_session=request.session.get("otp")
        if user_otp==otp_session:
            return render(request,'app/success.html')
        else:
            return render(request,'app/failure.html')
    return render(request,'app/verify_otp.html')