from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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

def mealCheck(request):
    
    
    
    
    return render(request,'mealCheck.html')



def exerciseCheck(request):
    data=[{'user': 'gong111', 'exercise': 'wa_3','ex_time':80,'burned':780,'goal':1000,'content':''},
          {'user': 'gong111', 'exercise': 'wa_4','ex_time':80,'burned':780,'goal':1000,'content':''},
          {'user': 'gong111', 'exercise': 'wa_5','ex_time':80,'burned':780,'goal':1000,'content':''}]
    # qs=Exercise.objects.all()
    content={'exerciseList':data}
    return render(request,'exerciseCheck.html',content)

def exercise1(request):
    data = [{'activity': 'bicycling', 'ex_name': '자전거','level':2},
            {'activity': 'running', 'ex_name': '조깅','level':3},
            {'activity': 'running', 'ex_name': '달리기','level':3},
            {'activity': 'walking', 'ex_name': '걷기','level':3},
            {'activity': 'walking', 'ex_name': '걷기','level':6},
            {'activity': 'sports', 'ex_name': '야구','level':6},
            {'activity': 'sports', 'ex_name': '농구','level':6},
            {'activity': 'health club exercise', 'ex_name': '풀업','level':6},
            {'activity': 'health club exercise', 'ex_name': '행잉레그레이즈','level':6},
            {'activity': 'health club exercise', 'ex_name': '레그프레스','level':6},
            {'activity': 'sports', 'ex_name': '축구','level':6}]
    
    data1=list({v['ex_name']:v for v in data}.values()) # ex_name이 같은데 level이 다르면 같은 이름을 여러번 프린트하게 되어서 중복제거를 해줘야함
    return JsonResponse(data1,safe=False)

def exercise2(request):
    data = [{'activity': 'bicycling', 'ex_name': '자전거','level':2},
            {'activity': 'running', 'ex_name': '조깅','level':3},
            {'activity': 'running', 'ex_name': '달리기','level':3},
            {'activity': 'walking', 'ex_name': '걷기','level':3},
            {'activity': 'walking', 'ex_name': '걷기','level':6},
            {'activity': 'sports', 'ex_name': '야구','level':6},
            {'activity': 'sports', 'ex_name': '농구','level':6},
            {'activity': 'health club exercise', 'ex_name': '풀업','level':6},
            {'activity': 'health club exercise', 'ex_name': '행잉레그레이즈','level':6},
            {'activity': 'health club exercise', 'ex_name': '레그프레스','level':6},
            {'activity': 'sports', 'ex_name': '축구','level':6}]
    
    # 입력한 날짜 자동으로 적용되는 코드 짜야함
    
    return JsonResponse(data,safe=False)

def saveBtn(request):
    # 칼로리등등 계산해서 저장해야함
    # 데일리 운동 화면에서 총 운동 시간/운동 횟수/1회 평균 운동 시간 연동해야함
    
    
    return redirect("/dailycheck/exerciseCheck/")
    


def myStatus(request):
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
    
    
    
    
   