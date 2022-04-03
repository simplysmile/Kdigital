class Test:
    tno=11
    tname='hi'
    tkor=11
    
    def __init__(self,a,b):
        self.tno=Test.tno
        self.tname=a
        self.tkor=b
    
    def __str__(self):
        return '{}\t{}\t{}'.format(self.tno,self.tname,self.tkor)    