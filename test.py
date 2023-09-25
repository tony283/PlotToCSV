import numpy as np
from PIL import Image
import plot2csv_utility as pu
#plot path
path = r"D:\\graph\\1.png"
#save path .csv
savepath=r"D:\\graph\\1.csv"
#axis boudary
xlo =4000
xhi = 398.14
yhi = 70
ylo=5
#step on x axis [step, tolerence],tolerence range(0,1) is a value that random pick step from step*(1-tolerence) to step*(1+tolerence)
step =[5,0.1]
#this should be defined which return a bool value where the plot color is true
def colorjudge(color):
        if(color[0]>240 and color[1]<10 and color[2]<10):
            return True
        else:
            return False
#these should not be changed
p = pu.Plot2CSV(xlo,xhi,ylo,yhi,step,colorjudge)
p.LoadImage(path)
p.Process(savepath)
