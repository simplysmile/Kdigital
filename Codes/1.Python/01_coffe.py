
from defs.coffee import *
while True:
    mainscreen()
    ch=chisNum()
    
    if ch ==1: #메뉴선택
        coffees()
    elif ch ==2: #이용권충전
        payplus()
    elif ch ==3: #결제
        payment()
    elif ch ==4: #매출 출력
        dayprint()
    elif ch ==0:#주문취소
        print('>>>>> 주문을 종료합니다 <<<<<')
        break
    else:
        print('>>> 다시 입력하세요 <<<')
        continue
    
