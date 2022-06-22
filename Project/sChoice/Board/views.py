from django.shortcuts import render,redirect
from Member.models import Members,Dailydata
from Board.models import ExerciseBoard,MealBoard
from django.core.paginator import Paginator
from django.db.models import F
import pandas as pd 
import json
import numpy as np
import matplotlib.pyplot as plt
from django.http import JsonResponse
import math
from datetime import date



# #쇼핑 추천 함수
def shop(request): 
    print()
    return render(request,'shop.html')

# shop.html page에 제품을 올려 주는 함수
def shopAjax(request): 
    # Data 파일 안에 있는 csv 불러 옴
    df = pd.read_csv("./Data/BEST_100.csv")
    print(df)
    # json 파일을 위한 dictionary 만들기
    js_item={}
    # csv을 json으로 바꾸기
    js = df.to_json()
    #json 읽고 오기
    js_item['json_data'] = json.loads(js)
    print(js_item['json_data'])
    #json 데이터 담아서 보내기
    context = {'json_item':js_item}
    # context = {'id':'aaa'}
    # print("TEST")
    return JsonResponse(context, safe=False)
#####################################################################

#운동 게시판
def exboard(request,nowpage):
    qs = ExerciseBoard.objects.order_by('-b_Group','b_Step')
    
    mypages=Paginator(qs,5)
    fList=mypages.get_page(nowpage)
    context={'board_list':fList,'nowpage':nowpage}
    
    return render(request,'exboard.html',context)

#운동 글쓰기
def exwrite(request,nowpage):
    if request.method=="GET":
        context={'nowpage':nowpage}
        return render(request,'exboardWrite.html',context)
    
    u_id=request.session['session_user_id']
    bmem=Members.objects.get(user_id=u_id)
    bispro=bmem.pro
    btitle=request.POST.get('title')
    bcontent=request.POST.get('content')
    bfile=request.FILES.get('multim',None)
    
    qs = ExerciseBoard(member=bmem,m_Pro=bispro,b_Title=btitle,b_Content=bcontent,b_File=bfile)
    qs.save()
    qs.b_Group=qs.b_No
    qs.save()
    return redirect('Board:exboard',nowpage)
    

#식단 게시판
def fdboard(request,nowpage):
    qs = MealBoard.objects.order_by('-b_Group','b_Step')
    mypages=Paginator(qs,5)
    fList=mypages.get_page(nowpage)
    context={'board_list':fList,'nowpage':nowpage}    
    return render(request,'fdboard.html',context)

#식단 글쓰기
def fdwrite(request,nowpage):
    if request.method=="GET":
        context={'nowpage':nowpage}
        return render(request,'fdboardWrite.html',context)
    
    u_id=request.session['session_user_id']
    bmem=Members.objects.get(user_id=u_id)
    bispro=bmem.pro
    btitle=request.POST.get('title')
    bcontent=request.POST.get('content')
    bfile=request.FILES.get('multim',None)
    
    qs = MealBoard(member=bmem,m_Pro=bispro,b_Title=btitle,b_Content=bcontent,b_File=bfile)
    qs.save()
    qs.b_Group=qs.b_No
    qs.save()
    return redirect('Board:fdboard',nowpage)


#운동 글 상세보기
def exView(request,bNo,nowpage):
    qs=ExerciseBoard.objects.get(b_No=bNo)
    context={'bNo':bNo,'nowpage':nowpage,'bitem':qs}
    return render(request,'exView.html',context)


#식단 글 상세보기
def fdView(request,bNo,nowpage):
    qs=MealBoard.objects.get(b_No=bNo)
    context={'bNo':bNo,'nowpage':nowpage,'bitem':qs}
    return render(request,'fdView.html',context)

##########
#글 수정
#운동
def exBUP(request,bNo,nowpage):
    if request.method=="GET":
        qs=ExerciseBoard.objects.get(b_No=bNo)
        context={'item':qs,'bNo':bNo,'nowpage':nowpage}
        return render(request,'exUP.html',context)

    qs=ExerciseBoard.objects.get(b_No=bNo)
    btitle=request.POST.get('title')
    bcontent=request.POST.get('content')
    bfile=request.FILES.get('multim',None)
    qs.b_Title=btitle
    qs.b_Content=bcontent
    if bfile:
        qs.b_File=bfile
    qs.save()

    return redirect('Board:exboard',nowpage)

#식단
def fdBUP(request,bNo,nowpage):
    if request.method=="GET":
        qs=MealBoard.objects.get(b_No=bNo)
        context={'item':qs,'bNo':bNo,'nowpage':nowpage}
        return render(request,'fdUP.html',context)

    qs=MealBoard.objects.get(b_No=bNo)
    btitle=request.POST.get('title')
    bcontent=request.POST.get('content')
    bfile=request.FILES.get('multim',None)
    qs.b_Title=btitle
    qs.b_Content=bcontent
    if bfile:
        qs.b_File=bfile
    qs.save()

    return redirect('Board:fdboard',nowpage)


##########
#글삭제
#운동
def exDel(request,bNo,nowpage):
    qs=ExerciseBoard.objects.get(b_No=bNo)
    qs.delete()
    return redirect('Board:exboard',nowpage)

#식단
def fdDel(request,bNo,nowpage):
    qs=MealBoard.objects.get(b_No=bNo)
    qs.delete()
    return redirect('Board:fdboard',nowpage)

#########
#답글달기
#운동
def exReply(request,bNo,nowpage):
    if request.method=="GET":
        qs=ExerciseBoard.objects.get(b_No=bNo)
        context={'item':qs,'nowpage':nowpage}
        return render(request,'exReply.html',context)
    
    else:
        tId=request.session['session_user_id']
        tTitle=request.POST.get('title')
        tContent=request.POST.get('content')
        tFile=request.FILES.get('file',None)
        tGroup=request.POST.get('group')
        tStep=int(request.POST.get('step'))+1
        tIndent=int(request.POST.get('indent'))+1
        tMember=Members.objects.get(user_id=tId)
        
        step_qs=ExerciseBoard.objects.filter(b_Group=tGroup,b_Step__gte=tStep)
        step_qs.update(b_Step=F('b_Step')+1)
        
        qs=ExerciseBoard(member=tMember,b_Title=tTitle,b_Content=tContent,b_File=tFile,b_Group=tGroup,b_Step=tStep,b_Indent=tIndent)
        qs.save()
        
        return redirect('Board:exboard',nowpage)

#식단
def fdReply(request,bNo,nowpage):
    if request.method=="GET":
        qs=MealBoard.objects.get(b_No=bNo)
        context={'item':qs,'nowpage':nowpage}
        return render(request,'fdReply.html',context)
    
    else:
        tId=request.session['session_user_id']
        tTitle=request.POST.get('title')
        tContent=request.POST.get('content')
        tFile=request.FILES.get('file',None)
        tGroup=request.POST.get('group')
        tStep=int(request.POST.get('step'))+1
        tIndent=int(request.POST.get('indent'))+1
        tMember=Members.objects.get(user_id=tId)
        
        step_qs=MealBoard.objects.filter(b_Group=tGroup,b_Step__gte=tStep)
        step_qs.update(b_Step=F('b_Step')+1)
        
        qs=MealBoard(member=tMember,b_Title=tTitle,b_Content=tContent,b_File=tFile,b_Group=tGroup,b_Step=tStep,b_Indent=tIndent)
        qs.save()
        
        return redirect('Board:fdboard',nowpage)
###############################
#데이터 분석
def yourbody(request):
    return render(request,'helthInfo.html')


#나이계산
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#나이 범위 지정
def age_category(olds):
    if olds<25:
        a_cate='18-24'
    elif olds<30:
        a_cate='25-29'
    elif olds<35:
        a_cate='30-34'
    elif olds<40:
        a_cate='35-39'
    elif olds<45:
        a_cate='40-44'
    elif olds<50:
        a_cate='45-49'
    elif olds<55:
        a_cate='50-54'
    elif olds<60:
        a_cate='55-59'
    elif olds<65:
        a_cate='60-64'
    elif olds<70:
        a_cate='65-69'
    elif olds<75:
        a_cate='70-74'
    elif olds<80:
        a_cate='75-79'
    else:
        a_cate='80 or older'
    return a_cate

#Ajax
#당뇨
def bmidiabet(request):
    if request.session['session_user_id']: #로그인 된 경우
        user=Members.objects.get(user_id=request.session['session_user_id'])#사용자
        user_age=calculate_age(user.birth)#사용자 나이
        user_category=age_category(user_age)#사용자 연령대
        user_goal_weight=user.goal_weight #목표 몸무게
        
        user_daily=Dailydata.objects.filter(user=user).order_by('-day_no')[0] #사용자 변화데이터
        print(user_daily)
        user_hieght=user_daily.height #사용자 키
        cur_bmi=user_daily.cur_bmi #현재BMI
        cur_bmi=math.trunc(cur_bmi)
        cur_weight=user_daily.cur_weight #현재몸무게
        
        # bmi 계산
        len = user_hieght/100
        user_bmi = float(user_goal_weight)/float(len*len) #목표 BMI
        user_bmi=math.trunc(user_bmi)
        
        #데이터프레임 읽어오기
        df=pd.read_csv('./static/bmi_data/bmi_data.csv')
        #bmi-age 피벗테이블:당뇨
        bmi_pv=pd.pivot_table(df,values='Diabetic',index='AgeCategory',columns='BMI_range')
        bmidp=bmi_pv*100
        
        cur_user_diabet=bmidp[cur_bmi][user_category] #현재 유병률
        cur_user_diabet=round(cur_user_diabet,1)
        goal_user_diabet=bmidp[user_bmi][user_category] #목표시 유병률
        goal_user_diabet=round(goal_user_diabet,1)
        differs=goal_user_diabet-cur_user_diabet #유병률 변화
        differs=round(differs,1)
        
        context={'cur_w':cur_weight,'cur_bmi':cur_bmi,'goal_w':user_goal_weight,'goal_bmi':user_bmi,'cur_dp':cur_user_diabet,'goal_dp':goal_user_diabet,'differs':differs}
    
    else: #로그인 안된 경우
        context={'msg':'회원 가입시 개인 목표 분석을 제공해드립니다'}
    return JsonResponse(context,safe=False)



#심장
def bmiheart(request):
    if request.session['session_user_id']: #로그인 된 경우
        user=Members.objects.get(user_id=request.session['session_user_id'])#사용자
        user_age=calculate_age(user.birth)#사용자 나이
        user_category=age_category(user_age)#사용자 연령대
        user_goal_weight=user.goal_weight #목표 몸무게
        
        user_daily=Dailydata.objects.filter(user=user).order_by('-day_no')[0] #사용자 변화데이터
        print(user_daily)
        user_hieght=user_daily.height #사용자 키
        cur_bmi=user_daily.cur_bmi #현재BMI
        cur_bmi=math.trunc(cur_bmi)
        cur_weight=user_daily.cur_weight #현재몸무게
        
        # bmi 계산
        len = user_hieght/100
        user_bmi = float(user_goal_weight)/float(len*len) #목표 BMI
        user_bmi=math.trunc(user_bmi)
        
        #데이터프레임 읽어오기
        df=pd.read_csv('./static/bmi_data/bmi_data.csv')
        #bmi-age 피벗테이블:당뇨
        bmi_pv=pd.pivot_table(df,values='HeartDisease',index='AgeCategory',columns='BMI_range')
        bmidp=bmi_pv*100
        
        cur_user_diabet=bmidp[cur_bmi][user_category] #현재 유병률
        cur_user_diabet=round(cur_user_diabet,1)
        goal_user_diabet=bmidp[user_bmi][user_category] #목표시 유병률
        goal_user_diabet=round(goal_user_diabet,1)
        differs=goal_user_diabet-cur_user_diabet #유병률 변화
        differs=round(differs,1)
        
        context={'cur_w':cur_weight,'cur_bmi':cur_bmi,'goal_w':user_goal_weight,'goal_bmi':user_bmi,'cur_dp':cur_user_diabet,'goal_dp':goal_user_diabet,'differs':differs}
    
    else: #로그인 안된 경우
        context={'msg':'회원 가입시 개인 목표 분석을 제공해드립니다'}
    return JsonResponse(context,safe=False)



#신장
def bmikidney(request):
    if request.session['session_user_id']: #로그인 된 경우
        user=Members.objects.get(user_id=request.session['session_user_id'])#사용자
        user_age=calculate_age(user.birth)#사용자 나이
        user_category=age_category(user_age)#사용자 연령대
        user_goal_weight=user.goal_weight #목표 몸무게
        
        user_daily=Dailydata.objects.filter(user=user).order_by('-day_no')[0] #사용자 변화데이터
        print(user_daily)
        user_hieght=user_daily.height #사용자 키
        cur_bmi=user_daily.cur_bmi #현재BMI
        cur_bmi=math.trunc(cur_bmi)
        cur_weight=user_daily.cur_weight #현재몸무게
        
        # bmi 계산
        len = user_hieght/100
        user_bmi = float(user_goal_weight)/float(len*len) #목표 BMI
        user_bmi=math.trunc(user_bmi)
        
        #데이터프레임 읽어오기
        df=pd.read_csv('./static/bmi_data/bmi_data.csv')
        #bmi-age 피벗테이블:당뇨
        bmi_pv=pd.pivot_table(df,values='KidneyDisease',index='AgeCategory',columns='BMI_range')
        bmidp=bmi_pv*100
        
        cur_user_diabet=bmidp[cur_bmi][user_category] #현재 유병률
        cur_user_diabet=round(cur_user_diabet,1)
        goal_user_diabet=bmidp[user_bmi][user_category] #목표시 유병률
        goal_user_diabet=round(goal_user_diabet,1)
        differs=goal_user_diabet-cur_user_diabet #유병률 변화
        differs=round(differs,1)
        
        context={'cur_w':cur_weight,'cur_bmi':cur_bmi,'goal_w':user_goal_weight,'goal_bmi':user_bmi,'cur_dp':cur_user_diabet,'goal_dp':goal_user_diabet,'differs':differs}
    
    else: #로그인 안된 경우
        context={'msg':'회원 가입시 개인 목표 분석을 제공해드립니다'}
    return JsonResponse(context,safe=False)