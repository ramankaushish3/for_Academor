from matplotlib import pyplot as pt
from matplotlib import style
x1=[1,2,3]
y1=[2,3,1]
x2=[5,6,7]
y2=[3,2,3]
style.use('ggplot')
pt.bar(x1,y1,color='yellow')
pt.bar(x2,y2,color='red')
pt.show()
