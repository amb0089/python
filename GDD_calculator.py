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
        self.day1 = self.GDDacc.append(sum(self.GDDlist[0:(1+self.GDDlist.index(0))]))
        




        # self.day2 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1]))
        # self.day3 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2]))
        # self.day4 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2])+int(self.GDDlist[3]))
        # self.day5 = self.GDDacc.append(int(self.GDDlist[0])+int(self.GDDlist[1])+int(self.GDDlist[2])+int(self.GDDlist[3])+int(self.GDDlist[4]))
        
       
        
    


    def official (self):
        
        self.pastlist.append(int(input("enter official avg temp of yesterday: ")))
        
        return self.pastlist

        
    def officialList(self):
        
        
        
        for i in range(len(self.pastlist)):        
                   
                        
            self.pastacc.append(sum(self.pastlist[0:(i+1)]))
       
            
            
        return self.pastacc 

    def officialCal (self):

        self.totalacc = max(self.pastacc)
       
        return self.totalacc              
    


    def pastclipyield(self):
        '''Predicts the clipping yield based on GDD
        '''
        for i in range(len(self.pastacc)):
            if self.apps==1:
                yld = 2.42 * (2.71828 **(-self.pastacc[i]/264.1)) * math.sin((3.14159*(self.pastacc[i]+808.6))/871.7)            
            elif self.apps>1 and self.pastacc[i] <= 300:
                yld = -0.60
            elif self.apps>1 and self.pastacc[i] > 300 and self.pastacc[i] <=400:
                yld = -0.25
            elif self.apps>1 and self.pastacc[i] > 400 and self.pastacc[i] <=600:
                yld = -0.10 
            elif self.apps>1 and self.pastacc[i] > 600:
                yld = 0 
 
            if yld > 0:
                yld == 0
                self.clipyld.append(yld)
            else:
                self.clipyld.append(yld)    
    
        return self.clipyld


       
    def model(self):
        
   
        pylab.title('Yield Data')
        pylab.plot(self.pastacc, self.clipyld)
        pylab.show()



green = TEModel()
x=0
while x < 1:

    #green.forecast()
    #green.forecastCal()
    #green.updateGDD()
    green.official()
    x +=1


green.officialList()
green.officialCal()
green.pastclipyield()
green.model()




#print(green.GDDlist)
#print(green.GDDacc)
print(green.pastlist)
print(green.pastacc)
print(green.totalacc)
print(green.clipyld)









