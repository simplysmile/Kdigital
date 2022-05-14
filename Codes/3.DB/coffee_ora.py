from dbdefs.cofeeDef import *
while True:
    print()
    print('[ id에 0 입력시 종료 ]')
    cid=input('아이디를 입력하세요 : ')
    if cid=='0':
        exit()
    cpw=input('비밀번호를 입력하세요 : ')
    check=login(cid,cpw)
    
    #로그인 성공시 주문 시작
    while check==1:
        mainscreen()
        ch=chisNum()
        
        if ch ==1: #메뉴선택
            coffees()
        elif ch ==2: #이용권충전
            payplus(cid)
        elif ch ==3: #결제
            payment()
        elif ch ==4: #매출 출력
            dayprint()
        elif ch ==0:#주문종료
            print('>>>>> 주문을 종료합니다 <<<<<')
            break
        else:
            print('>>> 다시 입력하세요 <<<')
            continue
    
