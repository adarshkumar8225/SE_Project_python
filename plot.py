import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
conn = sqlite3.connect('SE.db')
c1=conn.cursor()

def read_from_db():
    c1.execute("SELECT per_a,per_t,per_g,per_c FROM genetic")
    data = c1.fetchall()
    print(data)
    per=[]
    
    y1=data[0]
    y2=data[3]
    y3=data[4]
    x=['a','t','g','c']
    plt.plot(x,y1,'c')
    plt.plot(x,y2,'g')
    plt.plot(x,y3,'r')
    plt.title('percentage distribution')
    plt.ylabel('percentage')
    plt.xlabel('element of amino acid')
    plt.show()


read_from_db()
