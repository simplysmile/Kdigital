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
        print('QQQQQQQQQQQQ:',qs)
          
    elif category == 'user_id':
        qs = Members.objects.filter(user_id__contains=searchword).order_by('-user_name')
        print('QQQQQQQQQQQQ:',qs)
        
        
    elif category == 'email':
        qs = Members.objects.filter(email__contains=searchword).order_by('-user_name')
        print('QQQQQQQQQQQQ:',qs)
        
    else:
        qs = Members.objects.filter(Q(user_name__contains=searchword)|Q(user_id__contains=searchword)|Q(user_name__contains=searchword)).order_by('-user_name')
        print('QQQQQQQQQQQQ:',qs)
        
    context ={'admin_List':qs,'searchword':searchword,'category':category}
    
    return render(request,'ad_m_L.html',context)


def ad_m_V(request,user_id,searchword,category):
    
    qs = Members.objects.get(user_id=user_id)
    
    
    context ={'admin_List':qs,'searchword':searchword,'category':category}
    print(context)
    

    return render(request,'ad_m_V.html',context)