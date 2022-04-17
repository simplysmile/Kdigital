import json
from stumanage.defJ_0417 import *

while True:
    #print screen
    ch=screenprint()
    #input
    if ch ==1:
        stuInput()
    #modify
    elif ch ==2:
        stuModify()
    #delete
    elif ch ==3:
        stuDel()
    #printall
    elif ch ==4:
        stuAll()
    #searchprint
    elif ch==5:
        stuPrint()
    #rank
    elif ch==6:
        stuRank()
    elif ch==0:
        print('>>>>> 프로그램 종료 <<<<<')
        break
    else:
        print('>>> 입력이 잘못되었습니다 <<<')
        continue
    