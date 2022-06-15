from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from AdminPage.models import Exercise
from Member.models import Members,Dailydata
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
    return render(request,'calendar.html')

def mealCheck(request,sdate):
    
    
    print(sdate)
    
    return render(request,'mealCheck.html')



def exerciseView(request):
    
    
    return render(request,'exerciseUpdate.html')
def exerciseUpdate(request):
    
        return render(request,'exerciseUpdate.html')


def exerciseCheck(request,sdate):
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from dailycheck_dailyexercise"
    
    rows=my_cursor.execute(mySQL)
    print(rows)    
    data_list = []
    daily_list=[]
    count=0
    for row in rows:
        data_dic={}
        daily_dic={}
        data_dic['user_id'] = row[7]
        qs=Exercise.objects.get(ex_id=row[6])
        data_dic['ex_name'] = qs.ex_name
        data_dic['createdate'] = row[5]
        data_dic['goal_kcal'] = row[3]
        data_dic['burned_kcal'] = row[2]
        data_dic['ex_time'] = row[1]
        num = ''.join(row[4].read())
        nums=num.split(',')
        data_dic['ex_counts']=int(nums[0])*int(nums[1])
        data_list.append(data_dic)
        
        count+=1
        no='exB'+str(count)
        daily_dic['ex_no']=no
        daily_dic['ex_name'] = qs.ex_name
        daily_dic['ex_time'] = row[1]
        daily_dic['goal_kcal'] = row[3]
        daily_dic['burned_kcal'] = row[2]
        
        if ((int(row[2])/int(row[3]))*100)>=100:
            daily_dic['kcal_per']=100
        else:
            daily_dic['kcal_per'] = (int(row[2])/int(row[3]))*100
        
        daily_list.append(daily_dic)
        
    daily_list2 = sorted(daily_list, key = lambda item : (-item['kcal_per']))
        
    Oracles.oraclose(my_cursor,my_conn)
        
        
    with open('static/exercisetest.json','w') as f:
        json.dump(daily_list2,f)
    print(daily_list2)
    
    content={'exerciseList':data_list}
    return render(request,'exerciseCheck.html',content)

def exercise1(request):
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
    # data=Exercise.objects.all()
    # data_list=list(data.values())
    return JsonResponse(data_relist,safe=False)

def exercise2(request):
    my_conn=Oracles.oraconn()
    my_cursor=Oracles.oracs(my_conn)
    mySQL="select * from adminpage_exercise"
    
    rows=my_cursor.execute(mySQL)
    print(rows)    
    data_list = []
    for row in rows:
        data_dic={}
        data_dic['ex_id'] = row[0]
        data_dic['activity'] = row[1]
        data_dic['met'] = row[3]
        data_dic['level'] = row[4]
        data_dic['ex_name'] = row[5]
        
        data_dic['curr_date']=(datetime.datetime.now()).date() # 순간적으로 사용할 데이터일뿐
        data_list.append(data_dic)
        
    # 입력한 날짜 자동으로 적용되는 코드 짜야함
    Oracles.oraclose(my_cursor,my_conn)
    return JsonResponse(data_list,safe=False)

def saveBtn(request):
    # 칼로리등등 계산해서 저장해야함
    # 데일리 운동 화면에서 총 운동 시간/운동 횟수/1회 평균 운동 시간 연동해야함
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
        # data=Exercise.objects.all()
        # data_list=list(data.values())
        return JsonResponse(data_relist,safe=False)
    else:
        id=request.POST.get('id')
        member=Members.objects.get(user_id=id)
        ex_time=request.POST.get('ex_time')
        burned_kcal=request.POST.get('burned_kcal')
        
        goal_kcal=request.POST.get('goal_kcal')
        ex_id=request.POST.get('ex_id')
        exercise=Exercise.objects.get(exercise_id=ex_id)
        Dailydata=Dailydata.objects.get(user_id=id)
        
        # burned_kcal=int(exercise.met)*int(ex_time)*int(Dailydata.cur_weight)/60
    
        # burned_kcal=Exercise.met*time*(변화추이db.weight/60)
    
        return redirect("/dailycheck/exerciseCheck/")    
    

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
    
    
    
    
   
    
def addMealData(request):
    
    response_body = request.GET  
    meallist = dict(response_body.items())
    print(meallist)
    
    datalen = int(meallist['len'])
    mealtime = meallist['mealtime']
    
    i = 0
    
    for i in range(datalen):
        m_id = meallist['d['+str(i)+'][f_id]']
        m_name = meallist['d['+str(i)+'][f_name]']
        m_weight = meallist['d['+str(i)+'][f_weight]']
        m_cal = meallist['d['+str(i)+'][f_cal]']
        m_carb = meallist['d['+str(i)+'][f_carb]']
        m_prot = meallist['d['+str(i)+'][f_prot]']
        m_fat = meallist['d['+str(i)+'][f_fat]']
        arr =    [mealtime,m_id,m_name,m_weight,m_cal,m_carb,m_prot,m_fat]
        print(arr)
    data_list = []
    context={'data':data_list}
    
    return JsonResponse(context)





def setGoals(request):
    
    user_id= 'gong1111'
    qs = Members.objects.get(user_id=user_id)
    
    
    # my_conn=Oracles.oraconn()
    # my_cursor=Oracles.oracs(my_conn)
    # mySQL="select * from MEMBER_MEMBERS where user_id='"+user_id+"'"
    # rows=my_cursor.execute(mySQL)
    # for row in rows:
    #     rowlist = list(row)
    #     print(row) # 튜플 형식 
        
    
    # print(rowlist)

    
    
    qs2={'height':167, 'cur_weight': 55}
    
    context = {"user":qs, "duser":qs2}
    
    

    
    return render(request,'setGoals.html',context)
