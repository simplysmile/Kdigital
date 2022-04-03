class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuname,kor,eng):
        Student.stuno +=1
        self.stuno=Student.stuno
        self.stuname=stuname
        self.kor=kor
        self.eng=eng
        self.total=kor+eng
        self.avg=self.total/2
        self.rank=0
        
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
    
    def __eq__(self,other):
        return self.stuname==other
    
    def __lt__(self,other):
        return self.total<other.total
    
    def setKor(self,score):
        if score >=0:
            self.kor=score
            self.total=self.kor+self.eng
            self.avg=self.total/2
        else:
            print('>>> 입력이 잘못되었습니다 <<<')
    
    def setEng(self,score):
        if score >=0:
            self.eng=score
            self.total=self.kor+self.eng
            self.avg=self.total/2
        else:
            print('>>> 입력이 잘못되었습니다 <<<')
        
    def setRank(self,rank):
        self.rank=rank
    