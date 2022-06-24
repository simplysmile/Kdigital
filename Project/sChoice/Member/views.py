from django.shortcuts import redirect, render
from django.http import HttpResponse
from Member.models import Members,Dailydata
import datetime 

# 내 정보수정 함수
def mUpdate(request):
    user_id = request.session['session_user_id']
    if request.method =="GET":
        qs_member = Members.objects.get(user_id=user_id)
        
        qs_daily = Dailydata.objects.filter(user=qs_member).order_by('day_no')[0]
        print("ㅋㅣ",qs_daily)
        print("bmi",qs_daily.cur_bmi)
        print("bmi",qs_daily.cur_weight)
        
        context = {'update':qs_member,'update_daily':qs_daily}
        return render (request,'mUpdate.html',context)
    else:
        # 수정form에서 데이터 전달
        user_name = request.POST.get('user_name')
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender',None)
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        zipcode = request.POST.get('zipcode')
        addressd1 = request.POST.get('addressd1')
        addressd2 = request.POST.get('addressd2')
        service = request.POST.get('service')
        user_purpose = request.POST.get('user_purpose')
        user_target = request.POST.get('target')
        vegan= request.POST.get('vegan')
        pro = request.POST.get('advancelevel')
        goal_weight = request.POST.get('goal_weight')
        goal_bodyfat = request.POST.get('goal_bodyfat')
        goal_period = request.POST.get('goal_period')
        allergic_food = request.POST.get('activity')
        modidate = request.POST.get('modidate')
        height = request.POST.get('height')
        cur_weight = request.POST.get('cur_weight')
        

        

        # db에 수정저장
        qs_member = Members.objects.get(user_id=user_id)
        qs_daily = Dailydata.objects.filter(user=qs_member).order_by('day_no')[0]
        qs_daily.height = height
        qs_daily.cur_weight = cur_weight
        qs_daily.save()

        qs_member.user_name =  user_name
        qs_member.user_pw =  user_pw
        qs_member.birth =  birth
        qs_member.gender = gender
        qs_member.phone =  phone
        qs_member.email =  email
        qs_member.zipcode = zipcode
        qs_member.addressd1 =  addressd1
        qs_member.addressd2 =  addressd2
        qs_member.service =  service
        qs_member.user_purpose =  user_purpose
        qs_member.user_target =  user_target
        qs_member.vegan =  vegan
        qs_member.pro =  pro
        qs_member.goal_weight =  goal_weight
        qs_member.goal_bodyfat =  goal_bodyfat
        qs_member.goal_period =  goal_period
        qs_member.allergic_food =  allergic_food
        qs_member.modidate =  modidate

        qs_member.save()


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
    qs_member = Members.objects.get(user_id=user_id)
    qs_daily = Dailydata.objects.filter(user=qs_member).order_by('day_no')[0]
    context={'view':qs_member, 'view1':qs_daily}
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
    
    return render(request,'login.html')
    
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
        goal_weight = float(request.POST.get('goal_weight',None))
        goal_bodyfat= float(request.POST.get('goal_bodyfat',None))
        goal_period = int(request.POST.get('goal_period',None))
        height = float(request.POST.get('height',None))
        cur_weight = float(request.POST.get('weight',None))
        
        
        user = Members(user_id =user_id, user_pw = user_pw, user_name=user_name,pro=pro,birth=birth,gender=gender,phone=phone,email=email,zipcode=zipcode,addressd1=addressd1,\
            addressd2 = addressd2, addressd3 = addressd3, service=service,user_purpose=user_purpose, user_target=user_target, vegan=vegan, allergic_food=activity, goal_weight=goal_weight, goal_bodyfat=goal_bodyfat, goal_period= goal_period)
        
        user.save()
        
        
        
        ##BMI계산

        today = datetime.date.today()

        age = today.year-birth.year 
        age_month = today.month-birth.month 
        age_day = today.day-birth.day 

        if age_day<0:
            age_month -= 1
        if age_month<0:
            age -= 1



        # bmi 계산
        len = height/100
        bmi = float(cur_weight)/float(len*len)

        # bmr
        bmr = 0
        if gender=='male':
            bmr = (10*cur_weight) + (6.25*height) - (5*age) + 5
        else:
            bmr = (10*cur_weight) + (6.25*height) - (5*age) - 161


        activity = 1 # int(user.allergic_food)
        EERlist = [bmr * 1.2,bmr * 1.375,bmr * 1.55,bmr * 1.725,bmr * 1.9]
        amrlist = [EERlist[0]-bmr,EERlist[1]-bmr,EERlist[2]-bmr,EERlist[3]-bmr,EERlist[4]-bmr ]
        amr = round(amrlist[activity])
        eer = round(EERlist[activity])

        needcal = [eer,eer-250,eer-500,eer-1000]
        ch = user.service
        # ch = 'exercise'
        ex_ratio = 1     
        if ( ch =='exercise'):
            ex_ratio = 0.7 
        elif( ch =='blanace'):
            ex_ratio = 0.5 
        elif( ch =='meal'):
            ex_ratio = 0.3



        cut_weight = cur_weight - goal_weight
        total_cal = (7200 * cut_weight) / goal_period
        meal_cal = round(total_cal * (1-ex_ratio))
        ex_cal = round(total_cal * ex_ratio)


        shouldeatcal = needcal[0] - meal_cal
        
         ##BMI계산

        user2 = Dailydata(user=user, height = height, cur_weight=cur_weight,cur_bmi=bmi,goal_eat_kcal=shouldeatcal,goal_burn_kcal=ex_cal)

    
        user2.save()
        
        
        
        
        
            
        return redirect('/')