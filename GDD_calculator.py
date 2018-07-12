import random, pylab, math

class TEModel(object):
    '''Used to project clippings based on TE apps and weather
    '''
    def __init__(self):
        
        self.clipyld = []
        self.GDDlist = []
        self.apps = 3

        
    def GDDcal (self, GDD):
        '''pulls yesterday's weather data from dark sky
        '''
        self.GDD = GDD
        return self.GDD
        
    
        
    def updateGDD (self):
        
        self.GDDlist.append(self.GDD)
        
                
       
    def clipyield(self):
        '''Predicts the clipping yield based on GDD
        '''
        
        if self.apps==1:
            yld = 2.42 * (2.71828 **(-self.GDD/264.1)) * math.sin((3.14159*(self.GDD+808.6))/871.7)
        
        elif self.apps>1 and max(self.GDDlist) <= 300:
            yld = -0.60
        elif self.apps>1 and max(self.GDDlist) > 300 and max(self.GDDlist) <=400:
            yld = -0.25
        elif self.apps>1 and max(self.GDDlist) > 400 and max(self.GDDlist) <=600:
            yld = -0.10   
        elif self.apps>1 and max(self.GDDlist) > 600:
            yld = 0     
            
            
        if yld > 0:
            self.yld = 0
        else:
            self.yld = yld   
    
        return self.clipyld

    def updateyld (self):
        
        self.clipyld.append(self.yld)

        return self.clipyld
        
    def model(self):
        
    
        print(self.clipyld)
        print(self.GDDlist)
    
        pylab.title('Yield Data')
        pylab.plot(self.GDDlist, self.clipyld)
        pylab.show()



green = TEModel()
green.GDDcal(25)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()

green.GDDcal(50)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()

green.GDDcal(100)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.GDDcal(200)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()



green.GDDcal(300)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.GDDcal(400)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.GDDcal(500)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()



green.GDDcal(600)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()

green.GDDcal(700)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()


green.GDDcal(800)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()



green.GDDcal(900)
green.updateGDD()
green.clipyield()
green.updateyld()
green.model()







