from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from Member.models import Members
import datetime 

# Create your views here.
def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    
    
    if request.method == "GET":
        return render(request, 'signup.html')
    

    elif request.method == "POST":
        
        user_name = request.POST.get('username')
        user_id = request.POST.get('user_id')   
        user_pw  = request.POST.get('user_pw')
        re_pw  = request.POST.get('re_password')
        pro = request.POST.get('advancelevel')
        year  = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day  = int(request.POST.get('day'))
        birth = datetime.date(year,month,day)
        gender  = request.POST.get('gender')
        phone = request.POST.get('tel')
        email  = request.POST.get('email')
        zipcode = request.POST.get('postcode')
        addressd1 = request.POST.get('address')
        addressd2 = request.POST.get('detailAddress')
        addressd3 = request.POST.get('extraAddress')
        service= request.POST.get('service')
        user_purpose = request.POST.get('purpose')
        user_target = request.POST.get('target')
        vegan = request.POST.get('vegan')
        allergic_food  = request.POST.get('allergic_food')
        goal_weight = request.POST.get('goal_weight')
        goal_bodyfat= request.POST.get('goal_bodyfat')
        goal_period = request.POST.get('goal_period')
        
        
        user = Members(user_id =user_id, user_pw =make_password(user_pw),user_name=user_name,pro=pro,birth=birth,gender=gender,phone=phone,email=email,zipcode=zipcode,addressd1=addressd1,\
            addressd2 = addressd2, addressd3 = addressd3, service=service,user_purpose=user_purpose, user_target=user_target, vegan=vegan, allergic_food=allergic_food, goal_weight=goal_weight, goal_bodyfat=goal_bodyfat, goal_period= goal_period)
        
        user.save()
            
        return redirect('/')