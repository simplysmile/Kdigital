from datetime import datetime
from django.shortcuts import render,redirect
from Member.models import Members
from django.db.models import Q


#어바웃어스
def aboutus(request):
    return render(request,'aboutus.html')

#어드민페이지
def ad_m_L(request,searchword,category):
    
    if request.method == 'POST':
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        

    if category == 'user_name':
        qs = Members.objects.filter(user_name__contains=searchword).order_by('-user_name')
        
          
    elif category == 'user_id':
        qs = Members.objects.filter(user_id__contains=searchword).order_by('-user_name')
        
        
        
    elif category == 'email':
        qs = Members.objects.filter(email__contains=searchword).order_by('-user_name')
        
        
    else:
        qs = Members.objects.filter(Q(user_name__contains=searchword)|Q(user_id__contains=searchword)|Q(user_name__contains=searchword)).order_by('-user_name')
        
        
    context ={'admin_List':qs,'searchword':searchword,'category':category}
    
    return render(request,'ad_m_L.html',context)




#어드민 뷰페이지
def ad_m_V(request,user_id,searchword,category):
    
    qs = Members.objects.get(user_id=user_id)
    
    
    context ={'admin_List':qs,'searchword':searchword,'category':category}
    print('ccccccccccccccontext:',context)
    

    return render(request,'ad_m_V.html',context)


#어드민 write페이지
def ad_m_U(request,user_id,searchword,category):
    
    if request.method == 'GET':
        qs = Members.objects.get(user_id=user_id)
        context = {'ad_List':qs,'searchword':searchword,'category':category}
        
        return render(request,'ad_m_U.html',context)
    
    else:
        qs = Members.objects.get(user_id=user_id)
        
        qs.user_name = request.POST.get('username')
        qs.pro = request.POST.get('advancelevel')
        
        year  = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day  = int(request.POST.get('day'))
        
        qs.birth = datetime.date(year,month,day)
        qs.gender  = request.POST.get('gender')
        qs.phone = request.POST.get('tel')
        qs.email  = request.POST.get('email')
        qs.zipcode = request.POST.get('postcode')
        qs.addressd1 = request.POST.get('address')
        qs.addressd2 = request.POST.get('detailAddress')
        qs.addressd3 = request.POST.get('extraAddress')
        qs.service= request.POST.get('service')
        qs.user_purpose = request.POST.get('purpose')
        qs.user_target = request.POST.get('target')
        qs.vegan = request.POST.get('vegan')
        qs.allergic_food  = request.POST.get('allergic_food')
        qs.goal_weight = request.POST.get('goal_weight')
        qs.goal_bodyfat= request.POST.get('goal_bodyfat')
        qs.goal_period = request.POST.get('goal_period')
        
        qs.save()
        
        return redirect('AdminPage:ad_m_L',searchword,category)
       
        
    
    
    