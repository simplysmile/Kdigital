from stumanage.testC import Test
tSave=[]

def inputT():
    tname=input('이름을 입력 : ')
    tkor=int(input('점수입력 : '))
    tSave.append(Test(tname,tkor))

def printT():
    print('시험출력')
    for t in tSave:
        print(t)
        
