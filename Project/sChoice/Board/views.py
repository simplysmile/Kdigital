from django.shortcuts import render,redirect
from Member.models import Members
from Board.models import ExerciseBoard,MealBoard
import pandas as pd 
import json
import numpy as np
import matplotlib.pyplot as plt
from django.http import JsonResponse


#쇼핑 추천 함수
def shop(request): 
    return render(request,'shop.html')

# def shop(request): 
#     df = pd.read_csv("BEST_100.csv")
#     print(df)
#     js_item={}
#     js = df.to_json()
#     js_item['json_data'] = json.loads(js)
#     print(js_item['json_data'])
#     context = {'js_item':js_item}
#     return JsonResponse(context,safe=False)
    

#운동 게시판
def exboard(request):
    qs = ExerciseBoard.objects.order_by('-b_Group')
    context={'board_list':qs}
    
    
    return render(request,'exboard.html',context)

#운동 글쓰기
def exwrite(request):
    if request.method=="GET":
        return render(request,'exboardWrite.html')
    
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
    return redirect('Board:exboard')
    

#식단 게시판
def fdboard(request):
    qs = ExerciseBoard.objects.order_by('-b_Group')
    context={'board_list':qs}
    return render(request,'fdboard.html',context)

#식단 글쓰기
def fdwrite(request):
    if request.method=="GET":
        return render(request,'fdboardWrite.html')
    
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
    return redirect('Board:exboard')
    