from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from matplotlib.style import context
from AdminPage.models import Exercise
from Member.models import Members,Dailydata
from DailyCheck.models import Dailyexercise,DailyMeal
import json,datetime
import cx_Oracle
import pandas as pd
import numpy as np

# import jaydebeapi
# from dbdefs.oracleDef import *

class Oracles():

    username='ADMIN'
    password = 'Clouddata2022!'
  
    # # FOR MAC 
    # lib_dir = "/Users/jihyeon/instantclient_19_8/"
    # wallet_location = "/Users/jihyeon/instantclient_19_8/network/admin/Wallet_Guro.zip"
    # cx_Oracle.init_oracle_client(lib_dir)
    # jdbc_driver_loc = "/Library/Java/Extensions/ojdbc8/ojdbc8.jar"
    # jdbc ='jdbc:oracle:thin:@Guro_medium?TNS_ADMIN=//Users/jihyeon/instantclient_19_8/network/admin/Wallet_Guro'
    # jdbc_class ="oracle.jdbc.driver.OracleDriver"
 

    def oraconn():
        #  FOR WINDOWS 
        conn = cx_Oracle.connect(user='ADMIN', password='Clouddata2022!',dsn='Guro_medium')
        #  FOR MAC 
        # conn = jaydebeapi.connect(Oracles.jdbc_class,Oracles.jdbc,[Oracles.username, Oracles.password],Oracles.jdbc_driver_loc)
        return conn

    def oracs(conn):
        cs = conn.cursor()
        return cs

    def oraclose(cs,conn):
        cs.close()
        conn.close()




# Create your views here.

def calendar(request):
    return render(request,'calendar.html')
def calendarData(request):
    # 세션을 통해 아이디 
    u_id = request.session['session_user_id']
    # 아이디를 사용해서 정보를 얻는다. 
    user = Members.objects.get(user_id=u_id) # 멤버테이블
    
    today = datetime.date.today()
    curr_month = today.month
    curr_year = today.year
    
    
    # 로그인한 사용자의 데일리 운동 테이블과 데일리 식사 테이블 (해당 년, 월)
    exer = Dailyexercise.objects.filter(user=user, createdate__year=curr_year,createdate__month=curr_month)
    meal = DailyMeal.objects.filter(d_member=u_id, d_meal_date__year=curr_year,d_meal_date__month=curr_month)
    
    userDt = Dailydata.objects.filter(user=user,add_date__year=curr_year,add_date__month=curr_month)
    
    
    
    meal_data = {}
    exer_data={}
    user_data={}
    e_d = []
    e_c =[]
    m_d=[]
    m_c=[]
    u_d=[]
    u_im=[]
    u_w=[]
    for i in range(len(exer)):
        e_d.append(exer[i].createdate)
        e_c.append(exer[i].burned_kcal)
    for i in range(len(meal)):
        m_d.append(meal[i].d_meal_date)
        m_c.append(meal[i].d_kcal)
    
    for i in range(len(userDt)):
        u_d.append(userDt[i].add_date)
        if userDt[i].day_img:
            u_im.append(1)
        else:
            u_im.append(np.nan)
            
        if userDt[i].cur_weight:
            u_w.append(userDt[i].cur_weight)
        else:
            u_w.append(np.nan)
          
    
    
    meal_data['m_date']=m_d
    meal_data['m_cal']=m_c
    exer_data['ex_date']=e_d
    exer_data['ex_cal']=e_c
    user_data['u_date']=u_d
    user_data['u_im']=u_im
    user_data['u_w']=u_w
    
    df_meal = pd.DataFrame(meal_data)
    df_exer = pd.DataFrame(exer_data)
    df_user = pd.DataFrame(user_data)
    
    print(u_im)
 
    
    
    df_meal_sum = df_meal.groupby('m_date').sum()
    df_exer_sum = df_exer.groupby('ex_date').sum()

    js_meal = df_meal_sum.to_json()
    js_exer = df_exer_sum.to_json()
    js_user = df_user.to_json()
    
    body_json={}
    body_json['meal'] = json.loads(js_meal)
    body_json['exer'] = json.loads(js_exer)
    body_json['user'] = json.loads(js_user)
    
    context = {'body_json':body_json,'goaleatcal':userDt[0].goal_eat_kcal, 'goalburncal':userDt[0].goal_burn_kcal}
    return JsonResponse(context, safe=False)

def mealCheck(request,sdate):
    # 세션을 통해 아이디 
    u_id = request.session['session_user_id']
    user = Members.objects.get(user_id=u_id)
    
    # sdate안에 날짜 필터로 가져오기
    # ckdate = datetime.strptime(sdate, '%Y-%m-%d')
    # user_data = Dailydata.objects.filter(user=user,add_date__year=ckdate.year,add_date__month=ckdate.month,add_date__month=ckdate.day)
    # print(user_data.goal_eat_kcal)
    
    user_data = Dailydata.objects.filter(user=user).order_by('-add_date')
  
    
    
    # 사용자의 아이디와, 입력을 위해 클릭한 날짜 정보를 사용해서 쿼리를 얻는다. 
    # 사용자가, 그 날짜에 먹은 모든 식품을 가져온다. 
    breakfast_cal = [0]
    breakfast_c = [0]
    breakfast_p = [0]
    breakfast_f = [0]
    lunch_cal = [0]
    lunch_c = [0]
    lunch_p = [0]
    lunch_f = [0]
    dinner_cal = [0]
    dinner_c = [0]
    dinner_p = [0]
    dinner_f = [0]
    snack_cal = [0]
    snack_c = [0]
    snack_p = [0]
    snack_f = [0]
    b_cnt = 0
    l_cnt = 0
    d_cnt = 0
    s_cnt = 0
    qs_m = DailyMeal.objects.filter(d_member=u_id, d_meal_date=sdate)
    for i in range(qs_m.count()):
        print(qs_m[i])
        mtime = qs_m[i].d_meal_time
        # 아침 총 칼로리 (탄단지)
        if mtime=='B':
            breakfast_cal.append(qs_m[i].d_kcal)
            breakfast_c.append(qs_m[i].d_carb)
            breakfast_p.append(qs_m[i].d_protein)
            breakfast_f.append(qs_m[i].d_fat)
            b_cnt += 1
        # 점심 총 칼로리 (탄단지)
        if mtime=='L':
            lunch_cal.append(qs_m[i].d_kcal)
            lunch_c.append(qs_m[i].d_carb)
            lunch_p.append(qs_m[i].d_protein)
            lunch_f.append(qs_m[i].d_fat)
            l_cnt+=1
        # 저녁 총 칼로리 (탄단지)
        if mtime=='D':
            dinner_cal.append(qs_m[i].d_kcal)
            dinner_c.append(qs_m[i].d_carb)
            dinner_p.append(qs_m[i].d_protein)
            dinner_f.append(qs_m[i].d_fat)
            d_cnt += 1
        # 간식 총 칼로리 (탄단지)
        if mtime=='S':
            snack_cal.append(qs_m[i].d_kcal)
            snack_c.append(qs_m[i].d_carb)
            snack_p.append(qs_m[i].d_protein)
            snack_f.append(qs_m[i].d_fat)
            s_cnt += 1
            
            
    
    # print('아침칼로리',sum(breakfast_cal))
    context = {'sdate':sdate,
               'b_k':round(sum(breakfast_cal),2),
               'b_c':round(sum(breakfast_c),2),
               'b_p':round(sum(breakfast_p),2),
               'b_f':round(sum(breakfast_f),2),
               'l_k':round(sum(lunch_cal),2),
               'l_c':round(sum(lunch_c),2),
               'l_p':round(sum(lunch_p),2),
               'l_f':round(sum(lunch_f),2),
               'd_k':round(sum(dinner_cal),2),
               'd_c':round(sum(dinner_c),2),
               'd_p':round(sum(dinner_p),2),
               'd_f':round(sum(dinner_f),2),
               's_k':round(sum(snack_cal),2),
               's_c':round(sum(snack_c),2),
               's_p':round(sum(snack_p),2),
               's_f':round(sum(snack_f),2),
               'bcnt':b_cnt, 'lcnt':l_cnt, 'dcnt':d_cnt, 'scnt':s_cnt
    }
    
    
    
    # json for chart 필요한거 -> goal칼로리, 칼로리, 단백질 총량, 탄수화물총량, 지방총량 
    meal_json = {"goalCal":user_data[0].goal_eat_kcal, 
                 "totalCal":round((sum(breakfast_cal)+sum(lunch_cal)+sum(dinner_cal)+sum(snack_cal)),2), 
                 'carb':round((sum(breakfast_c)+sum(lunch_c)+sum(dinner_c)+sum(snack_c)),2),
                 'prot':round((sum(breakfast_p)+sum(lunch_p)+sum(dinner_p)+sum(snack_p)),2),
                 'fat':round((sum(breakfast_f)+sum(lunch_f)+sum(dinner_f)+sum(snack_f)),2)
                 }
    #-----------------------------------------------------------------------------------------
    #--------------------------  json part --------------------------------------------
    with open('static/mealjson.json','w') as f:
        json.dump(meal_json,f)
        
        
        
    print(context)
               
               
               
               
               
               
               
    
    return render(request,'mealCheck.html',context)

def imgDelete(request,sdate):
    u_id = request.session['session_user_id']
    date=sdate.split('-')
    curr_year=date[0]
    curr_month=date[1]
    curr_day=date[2]
    daily=Dailydata.objects.filter(user=u_id,add_date__year=curr_year,add_date__month=curr_month,add_date__day=curr_day)[0]
    daily.day_img=''
    daily.save()
    return redirect('DailyCheck:calendar')


def imgCheck(request,sdate):
    u_id = request.session['session_user_id']
    date=sdate.split('-')
    curr_year=date[0]
    curr_month=date[1]
    curr_day=date[2]
    if request.method=='POST':
        user = Members.objects.get(user_id=u_id)
        cur_weight=request.POST.get('weight')
        imgName= request.FILES.get('file',None)
        if Dailydata.objects.filter(user=u_id,add_date__year=curr_year,add_date__month=curr_month,add_date__day=curr_day):
            daily=Dailydata.objects.filter(user=u_id,add_date__year=curr_year,add_date__month=curr_month,add_date__day=curr_day)[0]
            cur_height=daily.height
            daily.cur_weight=cur_weight
            cur_bmi=float(float(cur_weight)//((float(cur_height)*0.01)**2))
            daily.cur_bmi=cur_bmi
            
            daily.day_img=imgName
            daily.save()
        else:
            qs = Dailydata.objects.filter(user=u_id).order_by('day_no')[0]
            cur_height=qs.height
            cur_bmi=float(float(cur_weight)//((float(cur_height)*0.01)**2))
            burned_kcal=qs.goal_burn_kcal
            eat_kcal=qs.goal_eat_kcal
            
            daily=Dailydata(user=user,height=cur_height,cur_weight=cur_weight,cur_bmi=cur_bmi,add_date=sdate,goal_burn_kcal=burned_kcal,goal_eat_kcal=eat_kcal)
            daily.save()
        
        return redirect('DailyCheck:calendar')

    else:
        if Dailydata.objects.filter(user=u_id,add_date__year=curr_year,add_date__month=curr_month,add_date__day=curr_day):
            daily=Dailydata.objects.filter(user=u_id,add_date__year=curr_year,add_date__month=curr_month,add_date__day=curr_day)[0]
            if not daily.day_img:
                day_img='/static/img/mem01.png'
            else:
                day_img=daily.day_img.url
            cur_weight = daily.cur_weight
            content={'day_img':day_img,'cur_weight':cur_weight,'sdate':sdate}
            data_relist=[content]
        else:
            content={'day_img':'/static/img/mem01.png','cur_weight':0,'sdate':sdate}
            data_relist=[content]
        return JsonResponse(data_relist,safe=False)
    
     
def exerciseDelete(request,sdate,ex_no):
    u_id = request.session['session_user_id']
    date=sdate.split('-')
    curr_year=date[0]
    curr_month=date[1]
    curr_day=date[2]
    daily=Dailyexercise.objects.get(user=u_id,ex_No=ex_no)
    daily.delete()
    url='/dailycheck/'+sdate+'/exerciseCheck/'
    
    return redirect(url)     

def exerciseUpdate(request,sdate,ex_no):
    if request.method=='POST':
        u_id=request.session['session_user_id']
        member=Members.objects.get(user_id=u_id)
        
        ex_name=request.POST.get('saveexercise')
        level=request.POST.get('savelevel') 
        exercise=Exercise.objects.get(ex_name=ex_name,level=level)
        
        ex_id=exercise.ex_id
        # 제일 최신 데이터를 쓰기 위해서 -day_no여야함
        Daily=Dailydata.objects.filter(user=u_id).order_by('-day_no')[0]
        
        ex_time2=request.POST.get('ex_time2') 
        ex_set2=request.POST.get('sets2') 
        ex_count=request.POST.get('counts2') 
        
        goal_kcal=request.POST.get('goal_kcal') 
        burned_kcal=int(exercise.met)*int(ex_set2)*int(ex_time2)*float(Daily.cur_weight)//60 
        content=ex_set2+','+ex_count 
        
        
        
        qs=Dailyexercise.objects.get(ex_No=ex_no)
        qs.level=level
        qs.ex_time=ex_time2
        qs.goal_kcal=goal_kcal
        qs.burned_kcal=burned_kcal
        qs.content=content
        
        qs.save()
        url='/dailycheck/'+sdate+'/exerciseCheck/'
    
        return redirect(url)   


# 수정 모달페이지를 불러오기위한 빌드업
def exerciseView(request,sdate,ex_no):
    u_id = request.session['session_user_id']
    date=sdate.split('-')
    curr_year=date[0]
    curr_month=date[1]
    curr_day=date[2]
    qs_m = Dailyexercise.objects.filter(user=u_id, createdate__year=curr_year,createdate__month=curr_month,createdate__day=curr_day)
    # 블럭에 뿌려주기랑 차트그리기로 만들기
    b_list = []
    for i in range(qs_m.count()):
        b_dic={}
        daily_dic={}
        b_dic['user_id'] = u_id
        b_dic['ex_id'] = qs_m[i].exercise
        
        ex_id= qs_m[i].exercise.ex_id
        qs=Exercise.objects.get(ex_id=ex_id)
        b_dic['ex_no'] = qs_m[i].ex_No
        b_dic['ex_name'] = qs.ex_name
        b_dic['goal_kcal'] = qs_m[i].goal_kcal
        b_dic['burned_kcal'] = qs_m[i].burned_kcal
        b_dic['ex_time'] = qs_m[i].ex_time
        
        b_dic['createdate'] = sdate
        num=qs_m[i].content
        nums=num.split(',')
        b_dic['ex_counts']=int(nums[0])*int(nums[1])
        b_list.append(b_dic)
        
    b_list2 = sorted(b_list, key = lambda item : (item['ex_no']))
    qs=Dailyexercise.objects.get(ex_No=ex_no)
    qs2=Exercise.objects.get(ex_id=qs.exercise_id)
    level= qs2.level
    ex_name= qs2.ex_name
    sc=(qs.content).split(',')
    ex_set=sc[0]
    ex_count=sc[1]
    content={'b_list':b_list2,'myList':qs,'sdate':sdate,'ex_no':ex_no,'level':level,'ex_name':ex_name,'ex_count':ex_count,'ex_set':ex_set}
    
    return render(request,'exerciseUpdate.html',content)


def exerciseCheck(request,sdate):
    u_id = request.session['session_user_id']
    date=sdate.split('-')
    curr_year=date[0]
    curr_month=date[1]
    curr_day=date[2]
    qs_m = Dailyexercise.objects.filter(user=u_id, createdate__year=curr_year,createdate__month=curr_month,createdate__day=curr_day)
    
    daily=Dailydata.objects.filter(user=u_id).order_by('day_no')[0]
    goal_burn_kcal=daily.goal_burn_kcal 
    
    # 블럭에 뿌려주기랑 차트그리기로 만들기
    b_list = []
    daily_list = []
    count=0
    for i in range(qs_m.count()):
        b_dic={}
        daily_dic={}
        b_dic['user_id'] = u_id
        b_dic['ex_id'] = qs_m[i].exercise
        
        ex_id= qs_m[i].exercise.ex_id
        qs=Exercise.objects.get(ex_id=ex_id)
        b_dic['ex_no'] = qs_m[i].ex_No
        b_dic['ex_name'] = qs.ex_name
        b_dic['goal_kcal'] = qs_m[i].goal_kcal
        b_dic['burned_kcal'] = qs_m[i].burned_kcal
        b_dic['ex_time'] = qs_m[i].ex_time
        
        
        b_dic['createdate'] = sdate
        num=qs_m[i].content
        nums=num.split(',')
        b_dic['ex_counts']=int(nums[0])*int(nums[1])
        b_list.append(b_dic)
        # 차트그리기
        count+=1
        no='exB'+str(count)
        daily_dic['ex_no']=no
        daily_dic['ex_name'] = qs.ex_name
        daily_dic['ex_time'] = int(qs_m[i].ex_time)*int(nums[0])
        daily_dic['goal_kcal'] = qs_m[i].goal_kcal
        daily_dic['burned_kcal'] = qs_m[i].burned_kcal
        daily_dic['total_burn_kcal']=goal_burn_kcal
        
        
        if ((int(qs_m[i].burned_kcal)/int(qs_m[i].goal_kcal))*100)>=100:
            daily_dic['kcal_per']=100
        else:
            daily_dic['kcal_per'] = (int(qs_m[i].burned_kcal)/int(qs_m[i].goal_kcal))*100
            
        
        daily_list.append(daily_dic)
        
    b_list2 = sorted(b_list, key = lambda item : (item['ex_no']))
    daily_list2 = sorted(daily_list, key = lambda item : (-item['kcal_per']))
    with open('static/exercisetest.json','w') as f:
        json.dump(daily_list2,f)


    # 모달창에서 뿌려주기
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from dailycheck_dailyexercise"
    rows=my_cursor.execute(mySQL)
    data_list = []
    daily_list=[]
    count=0
    for row in rows:
        data_dic={}
        daily_dic={}
        qs=Exercise.objects.get(ex_id=row[6])
        data_dic['ex_name'] = qs.ex_name
        data_list.append(data_dic)
    Oracles.oraclose(my_cursor,my_conn)
        
    user = Members.objects.get(user_id=u_id)  
    user_category=user.user_target
    user_category1=''
    if user_category=='abs':
        user_category1='복부'
    elif user_category=='arms':
        user_category1='팔'
    elif user_category=='chest':
        user_category1='가슴'
    elif user_category=='legs':
        user_category1='하체'
    elif user_category=='shoulders':
        user_category1='어깨'
    elif user_category=='all':
        user_category1='전신'
        
    content={'goal_burn_kcal':goal_burn_kcal,'b_list':b_list2,'exerciseList':data_list,'sdate':sdate,'user_category':user_category1}
    return render(request,'exerciseCheck.html',content)

def health_result(request):
    u_id = request.session['session_user_id']
    daily=Dailydata.objects.filter(user=u_id).order_by('day_no')[0]
    goal_burn_kcal=daily.goal_burn_kcal 
    # 나의 목표칼로리에 대한 운동테이블 출력
    exercise_qs=Exercise.objects.all()
    dailydata=Dailydata.objects.filter(user=u_id).order_by('-day_no')[0]
    health_list=[]
    for i in range(exercise_qs.count()//2):
        health_time0=int(goal_burn_kcal*60/float(dailydata.cur_weight)/float(exercise_qs[2*i].met))
        health_time1=int(goal_burn_kcal*60/float(dailydata.cur_weight)/float(exercise_qs[2*i+1].met))
        health_dic={}
        health_dic['health_time0']=health_time0
        health_dic['health_time1']=health_time1
        
        level0=exercise_qs[i*2].level
        level1=exercise_qs[2*i+1].level
        if level0==2:
            levelstr0='(저강도)'
        elif level0==3:
            levelstr0='(중강도)'
        else:
            levelstr0='(고강도)'
        if level1==2:
            levelstr1='(저강도)'
        elif level1==3:
            levelstr1='(중강도)'
        else:
            levelstr1='(고강도)'
        
        health_dic['ex_name0']=exercise_qs[i*2].ex_name 
        health_dic['ex_name1']=exercise_qs[2*i+1].ex_name 
        health_dic['level0']=levelstr0
        health_dic['level1']=levelstr1
        
        health_list.append(health_dic)
    return JsonResponse(health_list,safe=False)    
def aerobic(request):
    u_id = request.session['session_user_id']
    daily=Dailydata.objects.filter(user=u_id).order_by('day_no')[0]
    goal_burn_kcal=daily.goal_burn_kcal 
    # 유산소운동만 따로 분류하기
    exercise_aerobic=Exercise.objects.filter(aerobic='o')
    dailydata=Dailydata.objects.filter(user=u_id).order_by('-day_no')[0]
    aerobic_list=[]
    for i in range(exercise_aerobic.count()//2):
        
        health_time0=int(goal_burn_kcal*60/float(dailydata.cur_weight)/float(exercise_aerobic[2*i].met))
        health_time1=int(goal_burn_kcal*60/float(dailydata.cur_weight)/float(exercise_aerobic[2*i+1].met))
        health_dic={}
        health_dic['health_time0']=health_time0
        health_dic['health_time1']=health_time1
        
        level0=exercise_aerobic[i*2].level
        level1=exercise_aerobic[2*i+1].level
        if level0==2:
            levelstr0='(저강도)'
        elif level0==3:
            levelstr0='(중강도)'
        else:
            levelstr0='(고강도)'
        if level1==2:
            levelstr1='(저강도)'
        elif level1==3:
            levelstr1='(중강도)'
        else:
            levelstr1='(고강도)'
        
        health_dic['ex_name0']=exercise_aerobic[i*2].ex_name 
        health_dic['ex_name1']=exercise_aerobic[2*i+1].ex_name 
        health_dic['level0']=levelstr0
        health_dic['level1']=levelstr1
        
        aerobic_list.append(health_dic)
    return JsonResponse(aerobic_list,safe=False)    
def anaerobic(request):
    u_id = request.session['session_user_id']
    daily=Dailydata.objects.filter(user=u_id).order_by('day_no')[0]
    goal_burn_kcal=daily.goal_burn_kcal 
        
    # 웨이트만 따로 분류하기
    exercise_aerobic=Exercise.objects.filter(aerobic='x')
    dailydata=Dailydata.objects.filter(user=u_id).order_by('-day_no')[0]
    anaerobic_list=[]
    for i in range(exercise_aerobic.count()//2):
        
        health_time0=int(goal_burn_kcal*60/float(dailydata.cur_weight)/float(exercise_aerobic[2*i].met))
        health_time1=int(goal_burn_kcal*60/float(dailydata.cur_weight)/float(exercise_aerobic[2*i+1].met))
        health_dic={}
        health_dic['health_time0']=health_time0
        health_dic['health_time1']=health_time1
        
        level0=exercise_aerobic[i*2].level
        level1=exercise_aerobic[2*i+1].level
        if level0==2:
            levelstr0='(저강도)'
        elif level0==3:
            levelstr0='(중강도)'
        else:
            levelstr0='(고강도)'
        if level1==2:
            levelstr1='(저강도)'
        elif level1==3:
            levelstr1='(중강도)'
        else:
            levelstr1='(고강도)'
        
        health_dic['ex_name0']=exercise_aerobic[i*2].ex_name 
        health_dic['ex_name1']=exercise_aerobic[2*i+1].ex_name 
        health_dic['level0']=levelstr0
        health_dic['level1']=levelstr1
        
        anaerobic_list.append(health_dic)
    return JsonResponse(anaerobic_list,safe=False)    


def exercise1(request):
    u_id = request.session['session_user_id']
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from adminpage_exercise"
    rows=my_cursor.execute(mySQL)
    data_list = []
    for row in rows:
        data_dic={}
        data_dic['ex_name'] = row[5]
        data_dic['activity'] = row[1]
        data_dic['target_category']=row[6]
        if row[6]=='Abs':
            data_dic['target_category']='복부'
        elif row[6]=='Arms':
            data_dic['target_category']='팔'
        elif row[6]=='Chest':
            data_dic['target_category']='가슴'
        elif row[6]=='Legs':
            data_dic['target_category']='하체'
        elif row[6]=='Shoulders':
            data_dic['target_category']='어깨'
            
        data_list.append(data_dic)
    data_relist=list({v['ex_name']:v for v in data_list}.values())
    Oracles.oraclose(my_cursor,my_conn)
    return JsonResponse(data_relist,safe=False)

def exercise2(request):
    u_id = request.session['session_user_id']
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from adminpage_exercise"
    
    rows=my_cursor.execute(mySQL)
    data_list = []
    for row in rows:
        data_dic={}
        data_dic['user_id']=u_id
        data_dic['ex_id'] = row[0]
        data_dic['activity'] = row[1]
        data_dic['met'] = row[3]
        data_dic['level'] = row[4]
        data_dic['ex_name'] = row[5]
        
        data_list.append(data_dic)
        
    # 입력한 날짜 자동으로 적용되는 코드 짜야함
    Oracles.oraclose(my_cursor,my_conn)
    return JsonResponse(data_list,safe=False)

def saveBtn(request,sdate):
    u_id=request.session['session_user_id']
    member=Members.objects.get(user_id=u_id)
    if request.method=='GET':
        my_conn=Oracles.oraconn()
        my_cursor=Oracles.oracs(my_conn)
        mySQL="select * from adminpage_exercise"
        
        rows=my_cursor.execute(mySQL)
        data_list = []
        for row in rows:
            data_dic={}
            data_dic['ex_name'] = row[5]
            data_dic['activity'] = row[1]
            data_list.append(data_dic)
        
        data_relist=list({v['ex_name']:v for v in data_list}.values())
        Oracles.oraclose(my_cursor,my_conn)
        return JsonResponse(data_relist,safe=False)
    else:
        ex_name=request.POST.get('saveexercise')
        level=request.POST.get('savelevel')
        exercise=Exercise.objects.get(ex_name=ex_name,level=level)
        ex_id=exercise.ex_id
        
        Daily=Dailydata.objects.filter(user=u_id).order_by('-day_no')[0]
        ex_time2=request.POST.get('ex_time2')
        ex_set2=request.POST.get('sets2')
        ex_count=request.POST.get('counts2')
        
        goal_kcal=request.POST.get('goal_kcal')
        burned_kcal=int(exercise.met)*int(ex_set2)*int(ex_time2)*float(Daily.cur_weight)//60
        content=ex_set2+','+ex_count
        
        qs=Dailyexercise(user=member,exercise=exercise,createdate=sdate,ex_time=ex_time2,burned_kcal=burned_kcal,goal_kcal=goal_kcal,content=content)
        qs.save()
        url='/dailycheck/'+sdate+'/exerciseCheck/'
    
        return redirect(url)      
    
   
    

def myStatus(request):
    # 세션을 통해 아이디 
    # u_id = request.session['session_user_id']
    # 아이디를 사용해서 정보를 얻는다. 
    # user = Members.objects.get(user_id=u_id) # 멤버테이블
    
    # context={'username':user.user_name, "achievement":90}
    return render(request,'myStatus.html')

def myStatusData(request):
    # 세션을 통해 아이디 
    u_id = request.session['session_user_id']
    # 아이디를 사용해서 정보를 얻는다. 
    user = Members.objects.get(user_id=u_id) # 멤버테이블
    
    today = datetime.date.today()
    curr_month = today.month
    curr_year = today.year
    curr_day = today.day
    
    # 날짜 설정
    now = datetime.datetime.now()
    # idx = pd.date_range((now-datetime.timedelta(days=6)),now)
    idx = pd.date_range((now-datetime.timedelta(days=6)).strftime('%Y-%m-%d 00:00:00'),now.strftime('%Y-%m-%d 00:00:00'))
    
    
    
    # 로그인한 사용자의 데일리 운동 테이블과 데일리 식사 테이블 (해당 년, 월)
    meal = DailyMeal.objects.filter(d_member=u_id,d_meal_date__range=[today-datetime.timedelta(days=6), today])
    meal_all = DailyMeal.objects.filter(d_member=u_id)
    exer = Dailyexercise.objects.filter(user=user, createdate__range=[today-datetime.timedelta(days=6), today])
    exer_all = Dailyexercise.objects.filter(user=user)
    
    print('-----------------------------')
    exckday = exer_all.order_by('createdate')
    mealclday = meal_all.order_by('d_meal_date')
    
    firstexckday = exckday[0].createdate
    firstmealclday = mealclday[0].d_meal_date
    createantday = user.createdate
    dayarr = [firstexckday,firstmealclday,createantday]
      
    #  ----- 몸무게 달성 그래프 반 도넛 그래프를 위한 정보
    # 사용자 몸무게 데이터를 날짜 역순으로 가져온다. 
    userDt = Dailydata.objects.filter(user=user).order_by('-add_date')
    goal_meal_cal = userDt[0].goal_eat_kcal
    goal_burn_cal = userDt[0].goal_burn_kcal
    goal_weight = user.goal_weight
    goal_period = user.goal_period
    workoutdays = min(dayarr)
    
    start_date = datetime.date(workoutdays.year, workoutdays.month, workoutdays.day)
    target_date = datetime.date(curr_year, curr_month, curr_day)
    d_day = target_date - start_date
  

    allweight=[]
    alldays = []
    for i in range(len(userDt)):
        allweight.append(userDt[i].cur_weight)
        alldays.append(userDt[i].add_date.date())

    firstweight = userDt[len(userDt)-1].cur_weight
    #  ----- 몸무게 달성 그래프 반 도넛 그래프를 위한 정보 -end

    #  ----- 식단 정보 그래프 
    # 전체 날짜에 해당하는 내용
    mealstatus = {}
    mealdict={}
    m_d_a=[]
    m_c_a=[]
    m_cab_a=[]
    m_prt_a=[]
    m_fat_a=[]
    m_time_a=[]
    for i in range(len(meal_all)):
        m_d_a.append(meal_all[i].d_meal_date)
        m_c_a.append(meal_all[i].d_kcal)
        m_cab_a.append(meal_all[i].d_carb)
        m_prt_a.append(meal_all[i].d_protein)
        m_fat_a.append(meal_all[i].d_fat)
        m_time_a.append(meal_all[i].d_meal_time)
        
    mealstatus['m_date']=m_d_a
    mealstatus['m_cal']=m_c_a  
    df_meal_all = pd.DataFrame(mealstatus)
    df_meal_all_sum = df_meal_all.groupby('m_date').sum()
    avg_day_cal= round(df_meal_all_sum.mean()['m_cal'],2)
 

    meal_succ_day = 0
    
    for j in df_meal_all_sum.m_cal:
        if j <= goal_meal_cal:
            meal_succ_day+=1
    
    m_percent =  round(meal_succ_day/len(df_meal_all_sum) *100,2)
    
    mealdict['m_date']=m_d_a
    mealdict['m_cal']=m_c_a 
    mealdict['m_carb']=m_cab_a 
    mealdict['m_prot']=m_prt_a 
    mealdict['m_fat']=m_fat_a 
    mealdict['m_time']=m_time_a 
    df_mm = pd.DataFrame(mealdict)
    df_mm_day = df_mm.groupby('m_date').sum()
    df_mm_mealtime = df_mm.groupby('m_time').sum()
  
    total_b, total_l, total_d, total_s = 0,0,0,0
    if 'B' in df_mm_mealtime.index: 
        total_b = df_mm_mealtime.loc['B']['m_cal']
    if 'L' in df_mm_mealtime.index:
        total_l = df_mm_mealtime.loc['L']['m_cal']
    if 'D' in df_mm_mealtime.index:
        total_d = df_mm_mealtime.loc['D']['m_cal']
    if 'S' in df_mm_mealtime.index:
        total_s = df_mm_mealtime.loc['S']['m_cal']
    
    t_total= df_mm_mealtime['m_cal'].sum()
    bldstext = str(round(total_b/t_total *100 ))+':'+str(round(total_l/t_total *100 ))+':'+str(round(total_d/t_total *100 ))+':'+str(round(total_s/t_total *100 ))

    total_carb = df_mm['m_carb'].sum()
    total_prot = df_mm['m_prot'].sum()
    total_fat = df_mm['m_fat'].sum()
    total_total = total_carb+total_prot+total_fat
    ratiotxt = str(round(total_carb/total_total *10 ,1))+':'+str(round(total_prot/total_total *10 ,1))+':'+str(round(total_fat/total_total *10,1 ))
    
    
    
    

    
    d_avg_carb = df_mm_day['m_carb'].mean()
    d_avg_prot = df_mm_day['m_prot'].mean()
    d_avg_fat = df_mm_day['m_fat'].mean()
    
    
    
    mealinfo={'blds_ratio':bldstext,'cpf_ratio':ratiotxt,'avgCarb':d_avg_carb,'avgProt':d_avg_prot,'avgFat':d_avg_fat,'avgDCal':avg_day_cal}
    
    
    # 일주일 정보
    mdata={}
    m_d =[]
    m_c =[]

    for i in range(len(meal)):
        m_d.append(meal[i].d_meal_date.date())
        m_c.append(meal[i].d_kcal)


    mdata['m_date']=m_d
    mdata['m_cal']=m_c
    
    df_meal = pd.DataFrame(mdata)
    df_meal_sum = df_meal.groupby('m_date').sum()
    
    df_meal_sum.index = pd.DatetimeIndex(df_meal_sum.index)
    df_meal_sum = df_meal_sum.reindex(idx, fill_value=0)
    
    
    js_meal = df_meal_sum.to_json()

    # body_json={}
    # body_json['meal'] = json.loads(js_meal)
    
    

    



    #  ----- 식단 정보 그래프 -end 
    
    
    #  ----- 운동 정보 그래프 
     # 전체 날짜에 해당하는 내용
    exerstatus = {}
    e_d_a=[]
    e_c_a=[]
    e_t_a=[]
    e_n_a=[]
    e_isa=[]

    for i in range(len(exer_all)):
        e_d_a.append(exer_all[i].createdate.date())
        e_c_a.append(exer_all[i].burned_kcal)
        e_t_a.append(exer_all[i].ex_time)
        e_n_a.append(exer_all[i].exercise.ex_name)
        e_isa.append(exer_all[i].exercise.aerobic)
    exerstatus['m_date']=e_d_a
    exerstatus['m_cal']=e_c_a  
    exerstatus['e_time']=e_t_a  
    exerstatus['e_name']=e_n_a  
    exerstatus['e_isaerobic']=e_isa  
    df_exer_all = pd.DataFrame(exerstatus)
    df_exer_all_sum = df_exer_all.groupby('m_date').sum()



    exer_succ_day = 0
    
    for k in df_exer_all_sum.m_cal:
        if k <= goal_burn_cal:
            exer_succ_day+=1
    
    e_percent =  round(exer_succ_day/len(df_exer_all_sum) *100,2)

    num_usanso, num_musanso, time_usanso, time_musanso, cal_usanso, cal_musanso = 0,0,0,0,0,0


    if 'o' in df_exer_all.groupby('e_isaerobic').count().index: 
        num_usanso=df_exer_all.groupby('e_isaerobic').count()['e_time'].o
        time_usanso=df_exer_all.groupby('e_isaerobic').sum()['e_time'].o
        cal_usanso=df_exer_all.groupby('e_isaerobic').sum()['m_cal'].o
    if 'x' in df_exer_all.groupby('e_isaerobic').count().index:
        num_musanso=df_exer_all.groupby('e_isaerobic').count()['e_time'].x
        time_musanso=df_exer_all.groupby('e_isaerobic').sum()['e_time'].x
        cal_musanso=df_exer_all.groupby('e_isaerobic').sum()['m_cal'].x


    
 

    dfe = pd.DataFrame(exerstatus)
    dfe['m_date'] = pd.to_datetime(dfe['m_date'],format='%Y-%m-%d')
    dfe_sum = dfe.groupby('m_date').sum()
    mon_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 0').count()['e_time'])
    tue_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 1').count()['e_time'])
    wed_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 2').count()['e_time'])
    thr_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 3').count()['e_time'])
    fri_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 4').count()['e_time'])
    sat_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 5').count()['e_time'])
    sun_cnt = int(dfe_sum.query('m_date.dt.dayofweek == 6').count()['e_time'])



    df_exer_all_ename = df_exer_all.groupby('e_name').count()
    themostexer = df_exer_all_ename.idxmax()['m_date']


    

    exerinfo={'aerobic': [int(num_usanso),int(time_usanso),int(num_musanso),int(time_musanso),int(cal_usanso),int(cal_musanso)] ,
                'exerwk': [mon_cnt,tue_cnt,wed_cnt,thr_cnt,fri_cnt,sat_cnt,sun_cnt],'mostexer':themostexer }



    # 일주일 정보 ------------------------------------------------------
    edata={}
    e_d =[]
    e_c =[]       
    for i in range(len(exer)):
        e_d.append(exer[i].createdate.date())
        e_c.append(exer[i].burned_kcal)

    edata['m_date']=e_d
    edata['m_cal']=e_c
 
    # 데이터 프레임으로 만들기 => 날짜기준으로 칼로리 총합 구하기. 
    df_exer = pd.DataFrame(edata)
    df_exer_sum = df_exer.groupby('m_date').sum()
      
    
 

    df_exer_sum.index = pd.DatetimeIndex(df_exer_sum.index)
    df_exer_sum = df_exer_sum.reindex(idx, fill_value=0)
  
  
        
 
    
    
    
    
    
    
    
    js_exer = df_exer_sum.to_json()


    # print(df_exer)

    # print(df_exer_sum)

    #  ----- 운동 정보 그래프 -end 
    


    context={'goalEx':goal_burn_cal,'goalMeal':goal_meal_cal,'goal_weight':goal_weight,'goal_period':goal_period,
            'firstweight':firstweight,'workoutday':d_day.days, 'weight':allweight,'alldays':alldays,
            'Gmealcal':goal_meal_cal,'mealweak':json.loads(js_meal), 'mealpercent':m_percent,
            'Gexercal':goal_burn_cal,'exerweak':json.loads(js_exer), 'exerpercent':e_percent,
            'username':user.user_name, 'minfo':mealinfo, 'einfo':exerinfo
            }



    return JsonResponse(context)

    



def selfCheck(request):
    return render(request,'selfCheck.html')


@csrf_exempt
def searchMeal(request):   # food db에서 검색된 자료를 가져오는 함수
    if 'keyword' in request.GET:
        searchword = request.GET['keyword']
    # print(searchword)
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from adminpage_food where f_name like '%"+searchword+"%'"
    rows=my_cursor.execute(mySQL)
    data_list = []
    data_dic={}
    for row in rows:
        data_dic={}
        data_dic['f_id'] = row[0]
        data_dic['f_name'] = row[3]
        data_dic['f_weight'] = row[4]
        data_dic['f_carb'] = row[5]
        data_dic['f_prot'] = row[6]
        data_dic['f_fat'] = row[7]
        data_dic['f_cal'] = round(row[5]*4+row[6]*4+row[7]*9,2)
        data_list.append(data_dic)     
    # print(data_list)
    context={'data':data_list}
    Oracles.oraclose(my_cursor,my_conn)
    return JsonResponse(context)
    
    
    
    
@csrf_exempt   
def addMealData(request, sdate):

    #  세션을 통해서 사용자의 아이디를 가져온다
    u_id = request.session['session_user_id']
    #  사용자의 아이디를 이용해서 멤버내의 회원정보를 가져온다. 
    user = Members.objects.get(user_id=u_id)

    if request.GET: #   읽어오기. 업데이트하기.
        jsonData = request.GET  
        jData = dict(jsonData.items())

        mchoice = jData['mealSel']

        qs_m = DailyMeal.objects.filter(d_member=u_id, d_meal_date=sdate,d_meal_time=mchoice)

        
        dlist=[]

        for i in range(len(qs_m)):
            ddata={}
            ddata['f_id']=(qs_m[i].d_food)
            ddata['f_name']=(qs_m[i].d_food_name)
            ddata['f_weight']=(qs_m[i].d_por)
            ddata['f_carb']=(qs_m[i].d_carb)
            ddata['f_prot']=(qs_m[i].d_protein)
            ddata['f_fat']=(qs_m[i].d_fat)
            ddata['f_cal']=(qs_m[i].d_kcal)
            dlist.append(ddata)
            

        # print(f_id)
        # print(dlist)

        sendData = {'indata':dlist,'mealdate':sdate}

        return JsonResponse(sendData)

    elif request.POST: 

          
        # json 에서 가져온 입력 정보     
        response_body = request.POST  
        meallist = dict(response_body.items())

        # 총 입력 데이터 길이 (식품 몇개를 입력하는지 나타냄)
        datalen = int(meallist['len']) 
        # 현재 입력하고 있는 식사 시간(아침, 점심, 저녁, 간식)
        mealtime = meallist['mealtime']

        originalData = DailyMeal.objects.filter(d_member=u_id, d_meal_date=sdate,d_meal_time=mealtime)
        msg = ''
        if not originalData:
            # 만약에 원래 디비에 같은 정보가 없을 경우 .. 
            # 총 데이터의 길이만큼 db에 데이터를 넣어준다
            for i in range(datalen):
                m_id = meallist['d['+str(i)+'][f_id]']
                m_name = meallist['d['+str(i)+'][f_name]']
                m_weight = meallist['d['+str(i)+'][f_weight]']
                m_cal = meallist['d['+str(i)+'][f_cal]']
                m_carb = meallist['d['+str(i)+'][f_carb]']
                m_prot = meallist['d['+str(i)+'][f_prot]']
                m_fat = meallist['d['+str(i)+'][f_fat]']
                # arr =    [mealtime,m_id,m_name,m_weight,m_cal,m_carb,m_prot,m_fat]
                # print(arr)

                dmeal = DailyMeal(d_member = user, d_meal_date = sdate, d_meal_time=mealtime,d_food=m_id,d_food_name=m_name,d_por=m_weight,d_protein=m_prot,d_carb=m_carb,d_fat=m_fat,d_kcal=m_cal)
                dmeal.save()
            msg = '데이터를 성공적으로 저장하였습니다'
        else:
            DailyMeal.objects.filter(d_member=u_id, d_meal_date=sdate,d_meal_time=mealtime).delete()
            for i in range(datalen):
                m_id = meallist['d['+str(i)+'][f_id]']
                m_name = meallist['d['+str(i)+'][f_name]']
                m_weight = meallist['d['+str(i)+'][f_weight]']
                m_cal = meallist['d['+str(i)+'][f_cal]']
                m_carb = meallist['d['+str(i)+'][f_carb]']
                m_prot = meallist['d['+str(i)+'][f_prot]']
                m_fat = meallist['d['+str(i)+'][f_fat]']
                # arr =    [mealtime,m_id,m_name,m_weight,m_cal,m_carb,m_prot,m_fat]
                # print(arr)

                dmeal = DailyMeal(d_member = user, d_meal_date = sdate, d_meal_time=mealtime,d_food=m_id,d_food_name=m_name,d_por=m_weight,d_protein=m_prot,d_carb=m_carb,d_fat=m_fat,d_kcal=m_cal)
                dmeal.save()
            msg = '데이터를 성공적으로 수정하였습니다'



            

        context={'msg': msg}
        return JsonResponse(context)





def setGoals(request):

    #  세션을 통해서 사용자의 아이디를 가져온다
    u_id = request.session['session_user_id']
    #  사용자의 아이디를 이용해서 멤버내의 회원정보를 가져온다. 
    user = Members.objects.get(user_id=u_id)

    # dailydata db에서 키, 현재 몸무게 데이터를 가져온다
    user_data = Dailydata.objects.get(user=u_id, add_date=user.createdate)

    
    u_bmi=0
    u_bmr=0
    u_ex=0
    u_m=0
    # bmi = items['u_bmi']
    if 'u_bmi' in request.GET:
        u_bmi = float(request.GET['u_bmi'])
        u_bmr = float(request.GET['u_bmr'])
        u_ex = int(request.GET['u_ex_goal'])
        u_m = int(request.GET['u_m_goal'])
        
    
    
    
    print(u_bmi,u_bmr,u_ex,u_m)
   
    
    # --------------------------------------------------------------
    height = 165
    weight = 55
    goal_weight = 50
    gender = 'female'
    birth=user.birth

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
    bmi = float(weight)/float(len*len);
    
    bmr = 0
    if gender=='male':
        bmr = (10*weight) + (6.25*height) - (5*age) + 5
    else:
        bmr = (10*weight) + (6.25*height) - (5*age) - 161

    
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
    

    
    
    cut_weight = user_data.cur_weight - user.goal_weight
    total_cal = (7200 * cut_weight) / user.goal_period
    meal_cal = round(total_cal * (1-ex_ratio))
    ex_cal = round(total_cal * ex_ratio)
    
    
    shouldeatcal = needcal[0] - meal_cal
    
                
    
    # -----------------------------------------------------------------
    
    
    
    
    


    
    
    
    
    context = {"user":user, "duser":user_data}
    
    

    
    return render(request,'setGoals.html',context)



def delDailyMealData(request):
    if 'f_id' in request.GET:
        foodid = request.GET['f_id']
        
    if 'sdate' in request.GET:
        sdate = request.GET['sdate']
        
    if 'mealtime' in request.GET:
        mealtime = request.GET['mealtime']
        
    # 세션을 통해 아이디 
    u_id = request.session['session_user_id']
    delmeal = DailyMeal.objects.filter(d_member=u_id,d_meal_date=sdate,d_food=foodid,d_meal_time=mealtime)
    delmeal.delete()
    context={'msg':'성공적으로 삭제하였습니다.'}
    
    return JsonResponse(context)
