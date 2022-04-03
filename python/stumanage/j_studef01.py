import os
import json
#학생저장공간
stuSave=[]
#학생 번호 체크
sCount=0
#학생 존재 체크
count=0

#json읽어오기
def jRead():
    global stuSave
    if 'stuData.json' in os.listdir():
        stuSave=json.load(open('stuData.json','r'))
    else:
        stuSave=[]

#json저장하기
def jSave():
    json.dump(stuSave,open('stuData.json','w'))
    
#학생번호 증가
def setScount():
    global sCount
    if len(stuSave)==0:
        sCount=1
    else:
        sCount=stuSave[-1]['stuno']+1
    return sCount


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
        jRead()
        setScount()
        print('[  학생성적 입력  ]')
        print('-- {} 번 학생 입력'.format(sCount))
        stuname=input('학생 이름을 입력하세요(0. 입력종료) : ')
        if stuname=='0':
            break
        kor=int(input('국어점수를 입력하세요 : '))
        eng=int(input('영어점수를 입력하세요 : '))
        temp={'stuno':sCount,'stuname':stuname,'kor':kor,'eng':eng,'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
        stuSave.append(temp)
        jSave()
        print('-- {} 학생의 성적이 입력되었습니다.'.format(stuname))
    
#수정
def stuModify():
    print()
    print('[  학생성적 수정  ]')
    count=0
    jRead()
    search = input('대상 학생의 이름을 입력하세요 : ')
    for stu in stuSave:
        if stu['stuname']==search:
            count=1
            print('[  과목 선택  ]')
            print('1. 국어')
            print('2. 영어')
            print('-'*25)
            ch=chisNum()
            if ch==1:
                print('[  국어성적 수정  ]')
                print('현재 점수 : {}'.format(stu['kor']))
                score=int(input('변경점수를 입력하세요 : '))
                stu['kor']=score
                stu['total']=stu['kor']+stu['eng']
                stu['avg']=stu['total']/2
                jSave()
                print('-- {} 학생의 국어점수가 {} 점으로 변경되었습니다.'.format(search,score))
            elif ch==2:
                print('[  영어성적 수정  ]')
                print('현재 점수 : {}'.format(stu['eng']))
                score=int(input('변경점수를 입력하세요 : '))
                stu['eng']=score
                stu['total']=stu['kor']+stu['eng']
                stu['avg']=stu['total']/2
                jSave()
                print('-- {} 학생의 영어점수가 {} 점으로 변경되었습니다.'.format(search,score))
            else:
                print('>>> 입력이 잘못되었습니다 <<<')
    if count==0:
        print('-- {} 학생이 없습니다.'.format(search))

#삭제
def stuDel():
    print()
    jRead()
    print('[  학생성적 삭제  ]')
    count=0
    search = input('대상 학생의 이름을 입력하세요 : ')
    for i,stu in enumerate(stuSave):
        if stu['stuname']==search:
            count=1
            del(stuSave[i])
            jSave()
            print('-- {} 학생의 성적이 삭제되었습니다.'.format(search))
    if count==0:
        print('-- {} 학생이 없습니다.'.format(search))
        
            
#전체출력
def allPrint():
    jRead()
    title()
    for stu in stuSave:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],stu['total'],stu['avg'],stu['rank']))

#검색출력
def searchPrint():
    print()
    jRead()
    print('[  학생성적 검색출력  ]')
    count=0
    search = input('대상 학생의 이름을 입력하세요 : ')
    for stu in stuSave:
        if stu['stuname']==search:
            count=1
            title()
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],stu['total'],stu['avg'],stu['rank']))
            
    if count==0:
        print('-- {} 학생이 없습니다.'.format(search))
#등수처리
def stuRank():
    jRead()
    for stu1 in stuSave:
        rank=1
        for stu2 in stuSave:
            if stu1['total'] <stu2['total'] :
                rank +=1
        stu1['rank']=rank
        jSave()