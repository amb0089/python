import random, pylab, math

class TEModel(object):
    '''Used to project clippings based on TE apps and weather
    '''
    def __init__(self):
        
        self.clipyld = []
        self.GDDlist = []
        self.GDDacc = []
        self.pastlist = []
        self.pastacc = []
        self.apps = 1

        
    def forecast (self):
        '''pulls future weather data from dark sky, and calculates daily GDDs, future and previous day. Adds to list.
        '''
    
        x =0
        while x < 5:

            self.GDDlist.append(input("enter forecast avg: "))
            x+=1
        
        return self.GDDlist
        
    def forecastCal (self):
        self.day1 = self.GDDacc.append(int(self.GDDlist[0]))
        self.day2 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1]))
        self.day3 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2]))
        self.day4 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2])+int(self.GDDlist[3]))
        self.day5 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2])+int(self.GDDlist[3])+int(self.GDDlist[4]))
       
        
    


    def official (self):
        
        self.pastlist.append(int(input("enter official avg temp of yesterday: ")))
        
        return self.pastlist

        
    def officialList(self):
        
        x=1
        
        if x < len(self.pastlist):        
                      
            total = sum(self.pastlist[0:x])
            
            self.pastacc.append(total)
            x+=1
            # self.day2 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1]))
            # self.day3 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2]))
            # self.day4 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2])+int(self.GDDlist[3]))
            # self.day5 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2])+int(self.GDDlist[3])+int(self.GDDlist[4]))

        return self.pastacc 

    def officialCal (self):

        self.totalacc = max(self.pastacc)
       
        return self.totalacc              
    
    def clipyield(self):
        '''Predicts the clipping yield based on GDD
        '''
        
        if self.apps==1:
            yld = 2.42 * (2.71828 **(-self.totalacc/264.1)) * math.sin((3.14159*(self.totalacc+808.6))/871.7)
        elif self.apps>1 and self.totalacc <= 300:
            yld = -0.60
        elif self.apps>1 and self.totalacc > 300 and self.totalacc <=400:
            yld = -0.25
        elif self.apps>1 and self.totalacc > 400 and self.totalacc <=600:
            yld = -0.10 
        elif self.apps>1 and self.totalacc > 600:
            yld = 0 


            
        if yld > 0:
            self.yld = 0
        else:
            self.yld = yld   
    
        return self.yld

    def updateyld (self):
        
        self.clipyld.append(self.yld)

        return self.clipyld
       
    def model(self):
        
   
        pylab.title('Yield Data')
        pylab.plot(self.pastacc, self.clipyld)
        pylab.show()



green = TEModel()
x=0
while x < 5:

    #green.forecast()
    #green.forecastCal()
    #green.updateGDD()
    green.official()
    green.officialList()
    green.officialCal()
    green.clipyield()
    green.updateyld()
    x +=1

print(green.pastlist)
print(green.pastacc)



#green.model()

#print(green.GDDlist)
#print(green.GDDacc)
print(green.totalacc)

print(green.clipyld)




'''
green.forecast(50)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()

green.forecast(100)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.forecast(200)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()



green.forecast(300)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.forecast(400)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.forecast(500)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()



green.forecast(600)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()

green.forecast(700)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.forecast(800)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()



green.forecast(900)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()
'''






