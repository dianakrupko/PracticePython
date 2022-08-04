
import matplotlib.pyplot as plt
from numpy import double


def mnkLIN(x,y):
              a=round((len(x)*sum([x[i]*y[i] for i in range(0,len(x))])-sum(x)*sum(y))/(len(x)*sum([x[i]**2 for i in range(0,len(x))])-sum(x)**2),3)
              b=round((sum(y)-a*sum(x))/len(x) ,3)
              y1=[round(a*w+b ,3) for w in x]
              s=[round((y1[i]-y[i])**2,3) for i in range(0,len(x))]
              sko=round((sum(s)/(len(x)-1))**0.5,3)
              p=(sko*len(x)*100)/sum(y1)
              plt.title("Апроксимація методом найменших \n квадратів Y=%s*x+%s з похибкою  %i відсот."%(str(a),str(b),int(p)), size=14)
              plt.xlabel('Кількість міст', size=14)
              plt.ylabel('Довжина маршрутів', size=14)
              plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Дані методу найближчого сусіда')
              plt.plot(x, y1, color='b',linewidth=1, label='Апроксимуюча пряма')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()
              plt.savefig("graphic.png")

with open("file.json", 'r') as f:
    data = double(f.read().split('\n'))
    y=data
    x=[100,200,300,400,500,600,	700,800, 900,1000]
    mnkLIN(x,y)