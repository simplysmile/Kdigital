from stumanage.student01 import Student
#학생저장공간
stuSave=[]

#타이틀
def title():
    print()
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
    print('-'*60)
#선택숫자비교
def chisNum():
    ch=input('원하는 번호를 입력하세요 : ')
    if ch.isdigit():
        ch=int(ch)
    return ch
#화면출력
def screenPrint():
    print()
    print('-'*25)
    print('[  학생성적 관리  ]')
    print('1. 학생성적 입력')
    print('2. 학생성적 수정')
    print('3. 학생성적 삭제')
    print('4. 학생성적 전체출력')
    print('5. 학생성적 검색출력')
    print('6. 학생성적 등수처리')
    print('0. 프로그램 종료')
    print('-'*25)

#입력
def stuInput():
    while True:
        print()
        print('[  학생성적 입력  ]')
        stuname=input('학생 이름을 입력하세요(0. 입력종료) : ')
        if stuname=='0':
            break
        kor=int(input('국어점수를 입력하세요 : '))
        eng=int(input('영어점수를 입력하세요 : '))
        stuSave.append(Student(stuname,kor,eng))
        print('-- {} 학생의 성적이 입력되었습니다.'.format(stuname))
    
#수정
def stuModify():
    print()
    print('[  학생성적 수정  ]')
    count=0
    search = input('대상 학생의 이름을 입력하세요 : ')
    for stu in stuSave:
        if stu==search:
            count=1
            print('[  과목 선택  ]')
            print('1. 국어')
            print('2. 영어')
            print('-'*25)
            ch=chisNum()
            if ch==1:
                print('[  국어성적 수정  ]')
                print('현재 점수 : {}'.format(stu.kor))
                score=int(input('변경점수를 입력하세요 : '))
                stu.setKor(score)
                print('-- {} 학생의 국어점수가 {} 점으로 변경되었습니다.'.format(search,score))
            elif ch==2:
                print('[  영어성적 수정  ]')
                print('현재 점수 : {}'.format(stu.eng))
                score=int(input('변경점수를 입력하세요 : '))
                stu.setEng(score)
                print('-- {} 학생의 영어점수가 {} 점으로 변경되었습니다.'.format(search,score))
            else:
                print('>>> 입력이 잘못되었습니다 <<<')
    if count==0:
        print('-- {} 학생이 없습니다.'.format(search))

#삭제
def stuDel():
    print()
    print('[  학생성적 삭제  ]')
    count=0
    search = input('대상 학생의 이름을 입력하세요 : ')
    for i,stu in enumerate(stuSave):
        if stu==search:
            count=1
            del(stuSave[i])
            print('-- {} 학생의 성적이 삭제되었습니다.'.format(search))
    if count==0:
        print('-- {} 학생이 없습니다.'.format(search))
        
            
#전체출력
def allPrint():
    title()
    for stu in stuSave:
        print(stu)

#검색출력
def searchPrint():
    print()
    print('[  학생성적 검색출력  ]')
    count=0
    search = input('대상 학생의 이름을 입력하세요 : ')
    for stu in stuSave:
        if stu==search:
            count=1
            title()
            print(stu)
            
    if count==0:
        print('-- {} 학생이 없습니다.'.format(search))
#등수처리
def stuRank():
    for stu1 in stuSave:
        rank=1
        for stu2 in stuSave:
            if stu1<stu2:
                rank +=1
        stu1.setRank(rank)