coName=['아메핫','아아','라떼핫','라떼아이스']
coCost=[2000,2500,3000,3500] #커피가격
coCart=[0,0,0,0] #장바구니
daySell=[] #판매내역 리스트
allday=[0,0,0,0,0,0] #하루 총 매출
# sellName=['주문번호','아메핫','아아','라떼핫','라떼아이스','총판매액']
sellNo=0 #주문번호
mymoney=[0] #이용권금액

def chisNum():#번호선택
    ch =  input('원하는 번호를 입력하세요 :')
    if ch.isdigit():
        ch=int(ch)
    return ch

def cups():#잔수 선택
    cp=int(input('주문할 개수를 입력하세요 : '))
    return cp

def mainscreen():#메인페이지
    print()
    print('[  커피 주문  ]')
    print('1. 메뉴 선택')
    print('2. 이용권 충전')
    print('3. 결제')
    print('4. 매출내역')
    print('0. 주문 종료')
    print('-'*30)

def payplus():#이용권 충전
    print()
    print('[  이용권 충전  ]')
    print('잔여 금액 : {}'.format(mymoney[0]))
    plpay=int(input('충전할 금액을 입력하세요(원) : '))
    mymoney[0]=mymoney[0]+plpay
    print('충전 후 금액 : {}'.format(mymoney[0]))

def coffeeorder(ch):
    cp=cups()
    global coCart
    coCart[ch-1]=coCart[ch-1]+cp
    print('[  현재 주문 내역  ]')
    for i in range(4):
        if coCart[i]==0:
            continue
        print('-{} : {}잔'.format(coName[i],coCart[i]))

def coffees():#커피 주문
    while True:
        print()
        print('[  메뉴 선택  ]')
        print('1.아메핫')
        print('2.아아')
        print('3.라떼핫')
        print('4.라떼아이스')
        print('0.메뉴 선택 종료')
        print('-'*30)
        ch=chisNum()
        if ch==1:
            coffeeorder(ch)
        elif ch ==2:
            coffeeorder(ch)
        elif ch ==3:
            coffeeorder(ch)
        elif ch ==4:
            coffeeorder(ch)
            
        elif ch ==0:
            print('>>> 메뉴 선택을 종료합니다 <<<')
            break
        else:
            print('>>> 입력이 잘못되었습니다 <<<')
            continue

def payment():
    print('[  결제  ]')
    print('[  현재 주문 내역  ]')
    global coCart
    for i in range(4):
        if coCart[i]==0:
            continue
        print('-{} : {}잔'.format(coName[i],coCart[i]))
    totalCost=0
    for i in range(4):
        totalCost=totalCost+coCost[i]*coCart[i]
        
    if totalCost==0:
        print('>>> 선택된 메뉴가 없습니다 <<<')
    else:
        print('총 주문 금액 : {}'.format(totalCost))
        paych=input('- 주문하시겠습니까? [Y/N]')
        #Y/N주문동의
        if paych.lower()=='y':
            while mymoney[0]<totalCost:
                print('>>> 충전금액이 부족합니다 <<<')
                print('총 주문금액 : {}원'.format(totalCost))
                print('잔여 이용권 금액 : {}원'.format(mymoney[0]))
                print('부족한 금액 : {}원'.format(totalCost-mymoney[0]))
                print('-'*50)
                print('1. 충전 | 2.주문취소')
                ch=chisNum()
                if ch==1:
                    payplus()
                #금액부족 주문취소
                else:
                    print('>>> 주문을 취소합니다 <<<')
                    coCart=[0,0,0,0]
                    break
            if mymoney[0]>=totalCost:
                mymoney[0]=mymoney[0]-totalCost
                print('>>> 주문이 완료되었습니다 <<<')
                print('잔여 이용권 금액 : {}원'.format(mymoney[0]))
                global sellNo
                sellNo+=1
                temp=[sellNo,coCart[0],coCart[1],coCart[2],coCart[3],totalCost]
                daySell.append(temp)
                coCart=[0,0,0,0]
        #Y/N주문취소
        else:
            print('>>> 주문을 취소합니다 <<<')
            coCart=[0,0,0,0]

def dayprint():
    print()
    print('주문번호','아메핫','아아','라떼핫','라떼아이스','판매액',sep='\t')
    print('-'*70)
    for daycofee in daySell:
        print(daycofee[0],daycofee[1],daycofee[2],daycofee[3],daycofee[4],daycofee[5],sep='\t')
        allday[0]=daycofee[0]
        allday[1]+=daycofee[1]
        allday[2]+=daycofee[2]
        allday[3]+=daycofee[3]
        allday[4]+=daycofee[4]
        allday[5]+=daycofee[5]
    print('-'*70)
    print('-'*70)
    print('총건수','아메핫','아아','라떼핫','라떼아이스','총판매액',sep='\t')
    print('-'*70)
    print(allday[0],allday[1],allday[2],allday[3],allday[4],allday[5],sep='\t')
