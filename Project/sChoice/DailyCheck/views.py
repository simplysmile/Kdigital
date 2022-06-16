from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from matplotlib.style import context
from AdminPage.models import Exercise
from Member.models import Members,Dailydata
from DailyCheck.models import Dailyexercise,DailyMeal
import json,datetime
import cx_Oracle
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
    # 세션을 통해 아이디 
    u_id = request.session['session_user_id']
    # 아이디를 사용해서 정보를 얻는다. 
    user = Members.objects.get(user_id=u_id) # 멤버테이블
    # qs_ex = Dailyexercise.objects.get(user=u_id) # 데일리 운동 테이블
    # qs_m = DailyMeal.objects.get(d_member=u_id) # 데일리 식사 테이블 

    # print(qs_ex.burned_kcal)
    # print(qs_m.d_kcal)
    return render(request,'calendar.html')

def mealCheck(request,sdate):
    # 세션을 통해 아이디 
    u_id = request.session['session_user_id']
    # 사용자의 아이디와, 입력을 위해 클릭한 날짜 정보를 사용해서 쿼리를 얻는다. 
    # 사용자가, 그 날짜에 먹은 모든 식품을 가져온다. 
    qs_m = DailyMeal.objects.filter(d_member=u_id, d_meal_date=sdate)
    for i in range(qs_m.count()):
        print(qs_m[i].d_food_name)
    
 
    context = {'sdate':sdate}
    
    return render(request,'mealCheck.html',context)




def exerciseUpdate(request,sdate,ex_no):
    if request.method=='POST':
        u_id=request.session['session_user_id']
        member=Members.objects.get(user_id=u_id)
        
        ex_name=request.POST.get('saveexercise')
        level=request.POST.get('savelevel') 
        print(ex_name)
        print(level)
        exercise=Exercise.objects.get(ex_name=ex_name,level=level)
        
        ex_id=exercise.ex_id
        Daily=Dailydata.objects.filter(user=u_id).order_by('-add_date')[0]
        
        ex_time2=request.POST.get('ex_time2') 
        ex_set2=request.POST.get('sets2') 
        ex_count=request.POST.get('counts2') 
        
        goal_kcal=request.POST.get('goal_kcal') 
        burned_kcal=int(exercise.met)*int(ex_set2)*int(ex_time2)*int(Daily.cur_weight)//60 
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
    qs_m = Dailyexercise.objects.filter(user=u_id, createdate=sdate)
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
        print(qs_m[i].content)
        num=qs_m[i].content
        nums=num.split(',')
        b_dic['ex_counts']=int(nums[0])*int(nums[1])
        b_list.append(b_dic)
        
    
    qs=Dailyexercise.objects.get(ex_No=ex_no)
    qs2=Exercise.objects.get(ex_id=qs.exercise_id)
    level= qs2.level
    ex_name= qs2.ex_name
    sc=(qs.content).split(',')
    ex_set=sc[0]
    ex_count=sc[1]
    content={'b_list':b_list,'myList':qs,'sdate':sdate,'ex_no':ex_no,'level':level,'ex_name':ex_name,'ex_count':ex_count,'ex_set':ex_set}
    
    return render(request,'exerciseUpdate.html',content)


def exerciseCheck(request,sdate):
    u_id = request.session['session_user_id']
    qs_m = Dailyexercise.objects.filter(user=u_id, createdate=sdate)
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
        print(qs_m[i].content)
        num=qs_m[i].content
        nums=num.split(',')
        b_dic['ex_counts']=int(nums[0])*int(nums[1])
        b_list.append(b_dic)
        
        # 차트그리기
        count+=1
        no='exB'+str(count)
        daily_dic['ex_no']=no
        daily_dic['ex_name'] = qs.ex_name
        daily_dic['ex_time'] = qs_m[i].ex_time
        daily_dic['goal_kcal'] = qs_m[i].goal_kcal
        daily_dic['burned_kcal'] = qs_m[i].burned_kcal
        
        if ((int(qs_m[i].burned_kcal)/int(qs_m[i].goal_kcal))*100)>=100:
            daily_dic['kcal_per']=100
        else:
            daily_dic['kcal_per'] = (int(qs_m[i].burned_kcal)/int(qs_m[i].goal_kcal))*100
        daily_list.append(daily_dic)
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
        
    content={'b_list':b_list,'exerciseList':data_list,'sdate':sdate}
    return render(request,'exerciseCheck.html',content)

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
    print(rows)    
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
        Daily=Dailydata.objects.filter(user=u_id).order_by('-add_date')[0]
        ex_time2=request.POST.get('ex_time2')
        ex_set2=request.POST.get('sets2')
        ex_count=request.POST.get('counts2')
        
        goal_kcal=request.POST.get('goal_kcal')
        burned_kcal=int(exercise.met)*int(ex_set2)*int(ex_time2)*int(Daily.cur_weight)//60
        content=ex_set2+','+ex_count
        
        qs=Dailyexercise(user=member,exercise=exercise,createdate=sdate,ex_time=ex_time2,burned_kcal=burned_kcal,goal_kcal=goal_kcal,content=content)
        qs.save()
        url='/dailycheck/'+sdate+'/exerciseCheck/'
    
        return redirect(url)      
    

def myStatus(request):
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from MEMBER_DAILYDATA where user_id='gong1111'"
    rows=my_cursor.execute(mySQL)
    for row in rows:
        print(row)
    
    return render(request,'myStatus.html')



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
    
    
    
    
   
    
def addMealData(request, sdate):
    #  세션을 통해서 사용자의 아이디를 가져온다
    u_id = request.session['session_user_id']
    #  사용자의 아이디를 이용해서 멤버내의 회원정보를 가져온다. 
    user = Members.objects.get(user_id=u_id)
    # json 에서 가져온 입력 정보     
    response_body = request.GET  
    meallist = dict(response_body.items())

    # 총 입력 데이터 길이 (식품 몇개를 입력하는지 나타냄)
    datalen = int(meallist['len']) 
    # 현재 입력하고 있는 식사 시간(아침, 점심, 저녁, 간식)
    mealtime = meallist['mealtime']

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

        dmeal = DailyMeal(d_member = user, d_meal_date = sdate, d_meal_time=mealtime,d_food=m_id,d_food_name=m_name,d_por=m_weight,d_carb=m_carb,d_fat=m_fat,d_kcal=m_cal)
        dmeal.save()



    

    context={'msg': '성공적으로 저장되었습니다'}
    return JsonResponse(context)





def setGoals(request):

    #  세션을 통해서 사용자의 아이디를 가져온다
    u_id = request.session['session_user_id']
    #  사용자의 아이디를 이용해서 멤버내의 회원정보를 가져온다. 
    user = Members.objects.get(user_id=u_id)

    # dailydata db에서 키, 현재 몸무게 데이터를 가져온다
    user_data = Dailydata.objects.get(user=u_id, add_date=user.createdate)

    # print(user_data.cur_weight)


    # searchword = request.GET['bmr']
    
    userdataitems = dict(request.GET)
    
    
    items =dict( request.GET.items())


    
    print(items)


    
    
    
    
    context = {"user":user, "duser":user_data}
    
    

    
    return render(request,'setGoals.html',context)
