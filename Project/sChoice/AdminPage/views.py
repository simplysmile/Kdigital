import datetime
from django.shortcuts import render,redirect
from Member.models import Members
from AdminPage.models import Food,Exercise,ContactUs
from django.db.models import Q


#어바웃어스
def aboutus(request):
    return render(request,'aboutus.html')



#Admin login
def ad_login(request):
    if request.method=='GET':
        return render(request,'ad_login.html')
    
    else: 
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        
        if user_id == 'admin' and user_pw =='1234':
        
            try:
                qs = Members.objects.get(user_id=user_id,user_pw=user_pw)
                
            except Members.DoesNotExist: 
                qs = None 
                
            if qs:
                request.session['session_user_id']=qs.user_id
                request.session['session_user_name']=qs.user_name
               
                
                
                return render(request,'ad_m_L.html')
            else:
                
                msg="관리자만 로그인이 가능합니다."
                
         
                return render(request,'ad_login.html',{'msg':msg})
            
        else:
            msg="관리자만 로그인이 가능합니다."
            return render(request,'ad_login.html',{'msg':msg})
        
    
#Admin logout
def ad_logout(request):
    request.session.clear()
    return redirect('/') 
    


#Admin Contact Us 
def ad_contact_us(request):
    
    
    if request.method == 'GET':
        
        return render(request,'ad_contact_us.html')
    
    elif request.method == 'POST':
        
        c_name = request.POST.get('c_name',None)
        c_email = request.POST.get('c_email',None)
        c_tel = request.POST.get('c_tel',None)
        c_title = request.POST.get('c_title',None)
        c_content = request.POST.get('c_content',None)
        
        contact_us = ContactUs(c_name=c_name,c_email=c_email,c_tel=c_tel,c_title=c_title,c_content=c_content)
        
        contact_us.save()
        
        return redirect('/')


#Admin MEMBER List
def ad_m_L(request,searchword,category):
    
    if request.method == 'POST':
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        
    if category == 'category':
            qs = Members.objects.all().order_by('-user_name')
        

    elif category == 'user_name':
        qs = Members.objects.filter(user_name__contains=searchword).order_by('-user_name')
        
          
    elif category == 'user_id':
        qs = Members.objects.filter(user_id__contains=searchword).order_by('-user_name')
        
        
        
    elif category == 'email':
        qs = Members.objects.filter(email__contains=searchword).order_by('-user_name')
        
        
    else:
        qs = Members.objects.filter(Q(user_name__contains=searchword)|Q(user_id__contains=searchword)|Q(user_name__contains=searchword)).order_by('-user_name')
        
        
    context ={'admin_List':qs,'searchword':searchword,'category':category}
    
    return render(request,'ad_m_L.html',context)




#Admin MEMBER View
def ad_m_V(request,user_id,searchword,category):
    
    qs = Members.objects.get(user_id=user_id)
    
    
    context ={'admin_List':qs,'searchword':searchword,'category':category,'user_id':user_id}
  
    

    return render(request,'ad_m_V.html',context)


#Admin MEMBER Delete
def ad_m_D(request,user_id,searchword,category):
    
    qs = Members.objects.get(user_id=user_id)
    qs.delete()
    return redirect('AdminPage:ad_m_L',searchword,category)
    
    



#Admin MEMEBER Update
def ad_m_U(request,user_id,searchword,category):
    
    if request.method == 'GET':
        qs = Members.objects.get(user_id=user_id)
        
        context = {'ad_List':qs,'searchword':searchword,'category':category,'user_id':user_id}
        
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
    
###################################################################################
#admin FOOD List
def ad_f_L(request,searchword2,category2):
    
    if request.method == 'POST':
        category2 = request.POST.get('category2')
        searchword2 = request.POST.get('searchword2')
        
    # if category2 == 'category2':
    #     qs = Food.objects.all().order_by('-f_NO')
        
    if category2 == 'f_NO':
        qs = Food.objects.filter(f_NO__contains=searchword2).order_by('-f_NO')
        
          
    elif category2 == 'f_name':
        qs = Food.objects.filter(f_name__contains=searchword2).order_by('-f_NO')
        
        
        
    elif category2 == 'f_DB':
        qs = Food.objects.filter(f_DB__contains=searchword2).order_by('-f_NO')
        
        
    else:
        qs = Food.objects.filter(Q(f_NO__contains=searchword2)|Q(f_name__contains=searchword2)|Q(f_DB__contains=searchword2)).order_by('-f_NO')
        
        
    context ={'food_List':qs,'searchword2':searchword2,'category2':category2}
    
    return render(request,'ad_f_L.html',context)



#Admin Food View
def ad_f_V(request,f_NO,searchword2,category2):
    
    qs = Food.objects.get(f_NO=f_NO)
    
    
    context ={'Food_List':qs,'searchword2':searchword2,'category2':category2,'f_NO':f_NO}
    

    return render(request,'ad_f_V.html',context)



#Admin Food Update
def ad_f_U(request,f_NO,searchword2,category2):
    
    if request.method == 'GET':
        qs = Food.objects.get(f_NO=f_NO)
        
        context = {'food_List':qs,'searchword2':searchword2,'category2':category2,'f_NO':f_NO}
        
        return render(request,'ad_f_U.html',context)
    
    else:
        qs = Food.objects.get(f_NO=f_NO)
        
        qs.f_id = request.POST.get('f_id')
        qs.f_DB = request.POST.get('f_DB')
        qs.f_name  = request.POST.get('f_name')
        qs.f_por = request.POST.get('f_por')
        qs.f_carb  = request.POST.get('f_carb')
        qs.f_protein = request.POST.get('f_protein')
        qs.f_fat = request.POST.get('f_fat')
        
        qs.save()
        
        return redirect('AdminPage:ad_f_L',searchword2,category2)


#Admin Food Delete
def ad_f_D(request,f_NO,searchword2,category2):
    
    qs = Food.objects.get(f_NO=f_NO)
    
    print('@@@@@@@@@@@@@@@@@@@:',qs)
    
    qs.delete()
    
    return redirect('AdminPage:ad_f_L',searchword2,category2)   
    

###################################################################################
#admin EX List
def ad_e_L(request,searchword3,category3):
    
    if request.method == 'POST':
        category3 = request.POST.get('category3')
        searchword3 = request.POST.get('searchword3')
     
     
    if category3 == 'category3':
        qs = Exercise.objects.all().order_by('-ex_id')   
    
        
    elif category3 == 'ex_id':
        qs = Exercise.objects.filter(ex_id__contains=searchword3).order_by('-ex_id')
        
          
    elif category3 == 'ex_name':
        qs = Exercise.objects.filter(ex_name__contains=searchword3).order_by('-ex_id')
        
        
        
    elif category3 == 'level':
        qs = Exercise.objects.filter(level__contains=searchword3).order_by('-ex_id')
        
        
    else:
        qs = Exercise.objects.filter(Q(ex_id__contains=searchword3)|Q(ex_name__contains=searchword3)|Q(level__contains=searchword3)).order_by('-ex_id')
        
        
    context ={'ex_List':qs,'searchword3':searchword3,'category3':category3}
    
    return render(request,'ad_e_L.html',context)


#Admin EX View
def ad_e_V(request,ex_id,searchword3,category3):
    
    qs = Exercise.objects.get(ex_id=ex_id)
    
    
    context ={'ex_List':qs,'searchword3':searchword3,'category3':category3,'ex_id':ex_id}
    

    return render(request,'ad_e_V.html',context)



#Admin EX Delete
def ad_e_D(request,ex_id,searchword,category):
    
    qs = Exercise.objects.get(ex_id=ex_id)
    qs.delete()
    return redirect('AdminPage:ad_e_L',searchword,category)



#Admin EX Update
def ad_e_U(request,ex_id,searchword3,category3):
    
    if request.method == 'GET':
        qs = Exercise.objects.get(ex_id=ex_id)
        
        context = {'ex_List':qs,'searchword3':searchword3,'category3':category3,'ex_id':ex_id}
        
        return render(request,'ad_e_U.html',context)
    
    else:
        qs = Exercise.objects.get(ex_id=ex_id)
        
        qs.activity = request.POST.get('activity')
        qs.aerobic = request.POST.get('aerobic')
        qs.met  = request.POST.get('met')
        qs.level = request.POST.get('level')
        qs.ex_name  = request.POST.get('ex_name')
        qs.target_category = request.POST.get('target_category')
        qs.muscle = request.POST.get('muscle')
        qs.equipment = request.POST.get('equipment')
        
        qs.save()
        
        return redirect('AdminPage:ad_e_L',searchword3,category3)
    
    
###################################################################################



#Admin CONTACT List
def ad_c_L(request,searchword4,category4):
    
    if request.method == 'POST':
        category4 = request.POST.get('category4')
        searchword4 = request.POST.get('searchword4')
        
    if category4 == 'category4':
            qs = ContactUs.objects.all().order_by('-c_No')
        

    elif category4 == 'c_name':
        qs = ContactUs.objects.filter(c_name__contains=searchword4).order_by('-c_No')
        
          
    elif category4 == 'c_title':
        qs = ContactUs.objects.filter(c_title__contains=searchword4).order_by('-c_No')
        
        
        
    elif category4 == 'c_email':
        qs = ContactUs.objects.filter(c_email__contains=searchword4).order_by('-c_No')
        
        
    else:
        qs = ContactUs.objects.filter(Q(c_name__contains=searchword4)|Q(c_title__contains=searchword4)|Q(c_email__contains=searchword4)).order_by('-c_No')
        
        
    context ={'contact_List':qs,'searchword4':searchword4,'category4':category4}
    
    return render(request,'ad_c_L.html',context)


#Admin CONTACT View

def ad_c_V(request,c_No,searchword4,category4):
    
    qs = ContactUs.objects.get(c_No=c_No)
    
    
    context ={'c_List':qs,'searchword4':searchword4,'category4':category4,'c_No':c_No}
    

    return render(request,'ad_c_V.html',context)




#Admin CONTACT Update
def ad_c_U(request,c_No,searchword4,category4):
    
    if request.method == 'GET':
        
        qs = ContactUs.objects.get(c_No=c_No)
        
        context = {'c_List':qs,'searchword4':searchword4,'category4':category4,'c_No':c_No}
        
        return render(request,'ad_c_U.html',context)
    
    else:
        qs = ContactUs.objects.get(c_No=c_No)
        
        qs.c_name = request.POST.get('c_name')
        qs.c_title = request.POST.get('c_title')
        qs.c_email  = request.POST.get('c_email')
        qs.c_tel = request.POST.get('c_tel')
        qs.c_content = request.POST.get('c_content')
        qs.save()
        
        return redirect('AdminPage:ad_c_L',searchword4,category4)
    
    

#Admin CONTACT Delete
def ad_c_D(request,c_No,searchword4,category4):
    
    qs = ContactUs.objects.get(c_No=c_No)
    qs.delete()
    return redirect('AdminPage:ad_c_L',searchword4,category4)





