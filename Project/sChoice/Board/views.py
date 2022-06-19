from django.shortcuts import render,redirect
from Member.models import Members
from Board.models import ExerciseBoard,MealBoard
from django.core.paginator import Paginator
from django.db.models import F
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