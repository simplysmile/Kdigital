from stumanage.student01 import Student
from stumanage.studef01 import *

while True:
    screenPrint()
    ch=chisNum()
    if ch==1:
        stuInput()
    elif ch==2:
        stuModify()
    elif ch==3:
        stuDel()
    elif ch==4:
        allPrint()
    elif ch==5:
        searchPrint()
    elif ch==6:
        stuRank()
    elif ch==0:
        print('>>>>> 프로그램 종료 <<<<<')
        break
    else:
        print('>>> 입력이 잘못되었습니다 <<<')
    