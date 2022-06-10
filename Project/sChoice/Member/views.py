from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from Member.models import Members
import datetime 

# Create your views here.
def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        
        username = request.POST.get('username')   
        user_id = request.POST.get('user_id')   
        user_pw  = request.POST.get('user_pw')
        re_pw  = request.POST.get('re_password')
        pro = request.POST.get('re_password')
        
        year  = request.POST.get('year')
        month = request.POST.get('month')
        day  = request.POST.get('day')
        
        birth = datetime.date(year,month,day)
        
        gender  = request.POST.get('gender')
        phone = request.POST.get('phone')
        email  = request.POST.get('email')
        zipcode = request.POST.get('postcode')
        addressd1 = request.POST.get('address')
        addressd2 = request.POST.get('detailAddress')
        addressd3 = request.POST.get('extraAddress')
        
        service= request.POST.get('service')
        purpose = request.POST.get('purpose')
        vegan = request.POST.get('re_password')
        allergic_food  = request.POST.get('re_password')
        goal_weight = request.POST.get('re_password')
        goal_bodyfat= request.POST.get('re_password')
        goal_period = request.POST.get('re_password')
        
        
        res_data = {} 
        
        if not (username and  user_pw  and re_pw ):
            res_data['error'] = "필수정보를 입력해야 합니다."
            
        if user_pw != re_pw :
            
            res_data['error'] = '입력한 비밀번호가 일치하지 않습니다.'
        
        else :
            user = Members(birth= birth, user_id =user_id, user_pw =make_password(user_pw),user_name=username,pro=pro,birth=birth,gender=gender,phone=phone,email=email,zipcode=zipcode,addressd1=addressd1,\
                addressd2 = addressd2, addressd3 = addressd3, service=service,purpose=purpose,vegan=vegan, allergic_food=allergic_food, goal_weight=goal_weight,goal_bodyfat=goal_bodyfat,goal_period= goal_period)
            
            user.save()
            
        return render(request, 'signup.html', res_data)