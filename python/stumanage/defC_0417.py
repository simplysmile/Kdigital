from stumanage.stuC_0417 import Student


stuSave=[] #학생목록
count=0 #검색확인


#숫자판별
def isNum():
    ch = input('원하는 번호를 입력하세요 : ')
    if ch.isdigit():
        ch=int(ch)
    return ch

def screenprint():
    print()
    print('[  학생 성적 관리  ]')
    print('1. 학생성적 입력')
    print('2. 학생성적 수정')
    print('3. 학생성적 삭제')
    print('4. 학생성적 전체출력')
    print('5. 학생성적 검색출력')
    print('6. 학생성적 등수처리')
    print('0. 프로그램 종료')
    ch = isNum()
    return ch

#점수항목
def titlePrint():
    print()
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
    print('-'*55)


#input
def stuInput():
    print()
    print('[  학생 성적 입력  ]')
    stuname = input('학생 이름을 입력하세요 : ')
    kor = int(input('국어성적을 입력하세요 : '))
    eng = int(input('영어성적을 입력하세요 : '))
    stuSave.append(Student(stuname,kor,eng))

#modify
def stuModify():
    global count
    print()
    print('[  학생 성적 수정  ]')
    search = input('대상 학생의 이름을 입력하세요 : ')
    for stu in stuSave:
        if stu == search:
            count=1
            print('-- {} 학생이 검색되었습니다.'.format(search))
            print('[  수정 과목  ]')
            print('1. 국어 성적')
            print('2. 영어 성적')
            ch=isNum()
            if ch==1:
                print('현재 국어 성적 : {}'.format(stu.kor))
                score=int(input('변경 점수를 입력하세요 : '))
                stu.setKor(score)
                print('-- {} 학생의 국어 성적이 {} 으로 변경되었습니다.'.format(search,score))
            elif ch==2:
                print('현재 영어 성적 : {}'.format(stu.eng))
                score=int(input('변경 점수를 입력하세요 : '))
                stu.setEng(score)
                print('-- {} 학생의 영어 성적이 {} 으로 변경되었습니다.'.format(search,score))
            else:
                print('>>> 입력이 잘못되었습니다 <<<')
    if count == 0:
        print('-- {} 학생이 없습니다.'.format(search))
#delete
def stuDel():
    global count
    print()
    print('[  학생 성적 삭제  ]')
    search = input('대상 학생의 이름을 입력하세요 : ')
    for i,stu in enumerate(stuSave):
        if stu == search:
            count=1
            rch=input('-- 정말 {} 학생을 삭제하시겠습니까?(Y/N) : '.format(search))
            if rch.lower()=='y':
                del(stuSave[i])
                print('>>> {} 학생 성적이 삭제되었습니다 <<<'.format(search))
            else:
                print('-- {} 학생 성적 삭제가 취소되었습니다.'.format(search))
            
    if count == 0:
        print('-- {} 학생이 없습니다.'.format(search))

#printall
def stuAll():
    titlePrint()
    for stu in stuSave:
        print(stu)

#searchprint
def stuPrint():
    global count
    print()
    print('[  학생 성적 출력  ]')
    search = input('대상 학생의 이름을 입력하세요 : ')
    for stu in stuSave:
        if stu == search:
            count=1
            titlePrint()
            print(stu)
            
    if count == 0:
        print('-- {} 학생이 없습니다.'.format(search))

#rank
def stuRank():
    for stu1 in stuSave:
        rank=1
        for stu2 in stuSave:
            if stu1<stu2:
                rank+=1
        stu1.setRank(rank)
    print('>>> 등수처리가 완료되었습니다 <<<')