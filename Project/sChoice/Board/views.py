from django.shortcuts import render,redirect
from Member.models import Members
from Board.models import ExerciseBoard,MealBoard

def exboard(request):
    qs = ExerciseBoard.objects.order_by('-b_Group')
    context={'board_list':qs}
    
    
    return render(request,'infoTable.html',context)

def exwrite(request):
    if request.method=="GET":
        return render(request,'boardWrite.html')
    
    u_id=request.session.seession_id
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
    