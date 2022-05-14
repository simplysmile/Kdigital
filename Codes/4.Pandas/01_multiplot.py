import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']="AppleGothic"
matplotlib.rcParams['font.size']=10

df = pd.read_excel('score.xlsx')
df['국영수평균'] = (df['국어']+df['영어']+df['수학'])//3

x = df['이름']
y1 = df['국영수평균']
y2 = df['키']
y3 = df['과학']

plt.subplot(232)
plt.plot(x,y1,color='r')
plt.title('국영수 평균',fontsize=15)
plt.xlabel('이름',loc='right',color='g')
plt.ylabel('점수',loc='top',color='pink')

plt.subplot(234)
plt.barh(x,y2,label='키')
plt.title('학생-키',fontsize=15)
plt.xlim(150,210)
plt.legend()

plt.subplot(236)
plt.bar(x,y3,label='과학')
plt.title('과학성적',fontsize=15)
plt.ylim(20,110)
plt.legend()

plt.show()
