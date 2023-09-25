import numpy as np
from PIL import Image
import random

    

class Plot2CSV:
    def __init__(self,xlo,xhi,ylo,yhi,step,colorjudge):

        self.xlo = xlo
        self.ylo = ylo
        self.xhi=xhi
        self.yhi=yhi
        self.step = step

    def LoadImage(self,path):
        image = Image.open(path)
        self.image=np.array(image)

    def colorjudge(self,color):
        if(color[0]>240 and color[1]<10 and color[2]<10):
            return True
        else:
            return False

    def write2CSV(self,xl,yl,savepath):
        
        with open(savepath,'w') as f:
            for i in range(len(xl)):
                text = str(xl[i])+','+str(yl[i])+'\n'
                f.write(text)

    def Process(self,savepath):
        pix_x = self.image.shape[1]
        pix_y = self.image.shape[0]
        dx = abs(self.xhi-self.xlo)/pix_x
        dy = abs(self.yhi-self.ylo)/pix_y
        pix_step = [int(self.step[0]*(1-self.step[1])/dx),int(self.step[0]*(1+self.step[1])/dx)]
        
        pix_xlist =[]
        pix_ylist=[]
        n=0
        while(n<pix_x-1):
            pix_xlist.append(n)
            n+=random.randrange(pix_step[0],pix_step[1],1)
        pix_xlist.append(pix_x-1)
        for item in pix_xlist:
            first=0
            last=0
            startflag = False
            endflag = False
            for  i in range(pix_y):
                if(self.colorjudge(self.image[i,item]) and  startflag==False):
                    first=i
                    startflag = True
                if(startflag and  not self.colorjudge(self.image[i,item])):
                    last = i-1
                    endflag=True
                if(endflag):
                    break
            pix_ylist.append(int((first+last)/2))
        xlist = [item*dx*np.sign(self.xhi-self.xlo)+self.xlo   for item in pix_xlist]
        ylist = [self.yhi-self.ylo-item*dy*np.sign(self.yhi-self.ylo)   for item in pix_ylist]
        print(xlist)
        print(ylist)
        self.write2CSV(xlist,ylist,savepath)

                    



