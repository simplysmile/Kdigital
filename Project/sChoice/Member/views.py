from django.shortcuts import redirect, render
from django.http import HttpResponse
from Member.models import Members,Dailydata
import datetime 

# 내 정보수정 함수
def mUpdate(request):
    user_id = request.session['session_user_id']
    if request.method =="GET":
        qs = Members.objects.get(user_id=user_id)
        context = {'update':qs}
        return render (request,'mUpdate.html',context)
    else:
        # 수정form에서 데이터 전달
        user_name = request.POST.get('user_name')
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        zipcode = request.POST.get('zipcode')
        addressd1 = request.POST.get('addressd1')
        addressd2 = request.POST.get('addressd2')
        service = request.POST.get('service')
        user_purpose = request.POST.get('user_purpose')
        user_target = request.POST.get('user_target')
        vegan= request.POST.get('vegan')
        pro = request.POST.get('pro')
        goal_weight = request.POST.get('goal_weight')
        goal_bodyfat = request.POST.get('goal_bodyfat')
        goal_period = request.POST.get('goal_period')
        allergic_food = request.POST.get('allergic_food')
        modidate = request.POST.get('modidate')
        print(user_name)
        print(birth)
        print(allergic_food)

        # db에 수정저장
        qs = Members.objects.get(user_id=user_id)
        qs.user_name =  user_name
        qs.user_pw =  user_pw
        qs.birth =  birth
        qs.gender = gender
        qs.phone =  phone
        qs.email =  email
        qs.zipcode = zipcode
        qs.addressd1 =  addressd1
        qs.addressd2 =  addressd2
        qs.service =  service
        qs.user_purpose =  user_purpose
        qs.user_target =  user_target
        qs.vegan =  vegan
        qs.pro =  pro
        qs.goal_weight =  goal_weight
        qs.goal_bodyfat =  goal_bodyfat
        qs.goal_period =  goal_period
        qs.allergic_food =  allergic_food
        qs.modidate =  modidate
        qs.save()
        return redirect('Member:mView')

# 회원 삭제 함수
def mDelete(request):
    user_id = request.session['session_user_id']
    qs = Members.objects.get(user_id=user_id)
    qs.delete()
    request.session.clear()
    
    return redirect('/')

# 회원 읽기 함수
def mView(request):
    user_id = request.session['session_user_id']
    print(user_id)
    qs = Members.objects.get(user_id=user_id)
    qs.save()
    context={'view':qs}
    return render(request,'mView.html',context)


## 로그인 함수
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else: 
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

        # DB에서 id,pw 검색
        try:
            qs = Members.objects.get(user_id=user_id,user_pw=user_pw)
        except Members.DoesNotExist: 
            qs = None 
        if qs:
            request.session['session_user_id']=qs.user_id
            request.session['session_user_name']=qs.user_name
            return redirect('/')
        else:
            #user_id,user_pw 존재하지 않을 때
            msg="아이디 또는 패스워드가 일치하지 않습니다. \\n 다시 로그인해주세요.!!"
            return render(request, 'login.html',{'msg':msg})
    
# logout 함수        
def logout(request):
    request.session.clear()
    return redirect('/')    
#######################################################


def cancel_signup(request):
    
    return redirect('Member:signup')

def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    
    
    if request.method == "GET":
        return render(request, 'signup.html')
    

    elif request.method == "POST":
        
        user_name = request.POST.get('username', None)
        user_id = request.POST.get('user_id',None)   
        user_pw  = request.POST.get('user_pw',None)
        re_pw  = request.POST.get('re_password',None)
        pro = request.POST.get('advancelevel',None)
        year  = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day  = int(request.POST.get('day'))
        birth = datetime.date(year,month,day)
        gender  = request.POST.get('gender',None)
        phone = request.POST.get('tel',None)
        email  = request.POST.get('email',None)
        zipcode = request.POST.get('postcode',None)
        addressd1 = request.POST.get('address',None)
        addressd2 = request.POST.get('detailAddress',None)
        addressd3 = request.POST.get('extraAddress',None)
        service= request.POST.get('service',None)
        user_purpose = request.POST.get('purpose',None)
        user_target = request.POST.get('target',None)
        vegan = request.POST.get('vegan',None)
        activity  = request.POST.get('activity',None)
        goal_weight = request.POST.get('goal_weight',None)
        goal_bodyfat= request.POST.get('goal_bodyfat',None)
        goal_period = request.POST.get('goal_period',None)
        height = request.POST.get('height',None)
        cur_weight = request.POST.get('weight',None)
        
        
        user = Members(user_id =user_id, user_pw = user_pw, user_name=user_name,pro=pro,birth=birth,gender=gender,phone=phone,email=email,zipcode=zipcode,addressd1=addressd1,\
            addressd2 = addressd2, addressd3 = addressd3, service=service,user_purpose=user_purpose, user_target=user_target, vegan=vegan, allergic_food=activity, goal_weight=goal_weight, goal_bodyfat=goal_bodyfat, goal_period= goal_period)
        
        user.save()
        
        user2 = Dailydata(user=user, height = height, cur_weight=cur_weight)
        
        user2.save()
        
        
            
        return redirect('/')