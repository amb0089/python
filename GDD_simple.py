import random, pylab, math
import forecastio
from datetime import datetime, timedelta
import pylab
import argparse


class TEModel(object):
    '''Used to project clippings based on TE apps and weather
    '''
    def __init__(self):
        
        self.month = 7
        self.day = 16

        self.apps = 1
        self.freq = 300

        self.forecastdate = []
        self.forecastlist = []
        self.forecastacc = []
        
        self.pastdate = []        
        self.pastlist = []
        self.pastacc = []
        
        self.clipyld = []

        


    def official (self):
        
        api_key = "0e7bfbdbefec8029968ab7246e77150f"
        
        
        start = datetime(2018, self.month, self.day)
        end = datetime.now()
        
        times = [start]
        
        while start < end + timedelta(days=14):
            start += timedelta(days=1)
            times.append(start)

        lat =  32.593357 
        lng = -85.495163
    
        date = []
        temphigh = []
        templow = []
        
        for i in times:
            
            day1 = times[times.index(i)]

            location = forecastio.load_forecast(api_key, lat, lng, day1, units = "si")
                
            
            
            
            day = location.daily()
        
            for i in day.data[:]:
                temphigh.append(day.data[day.data.index(i)].d['temperatureHigh'])
                templow.append(day.data[day.data.index(i)].d['temperatureLow'])
                date.append(day.data[day.data.index(i)].time)
                
        both = [temphigh] + [templow]
    
        self.list = [(x+y)/2 for x,y in zip(*both)]
        self.date = date

        self.pastlist = self.list[0:-15]
        self.forecastlist = self.list[-15:]
        self.forecastdate = self.date[-15:]
            
        return self.pastlist, self.forecastlist

        
    def officialList(self):
        
        
        
        for i in range(len(self.pastlist)):        
                   
                        
            self.pastacc.append(sum(self.pastlist[0:(i+1)]))
       
            
            
        return self.pastacc 



    def forecastCal (self):
        
        listacc = []
        
        for i in range(len(self.list)):        
                    
                        
            listacc.append(sum(self.list[0:(i+1)]))
        
        self.forecastacc = listacc[-15:]
        
            
        return self.forecastacc     
        
    

    def officialCal (self):

        self.totalacc = max(self.pastacc)
       
        return self.totalacc

    
                      
                                    
                                                  
    def offreap(self):
                     
         
        if self.totalacc > self.freq:
            print("reapply now")

        else:
            for i in self.forecastacc:
                if i > self.freq:
                    index = self.forecastacc.index(i)
                    print("reapply on: " + str(self.forecastdate[index]))
                    print("Total GDD accumulation is: " + str(self.totalacc))
                    break



green = TEModel()
green.official()
green.officialList()
green.forecastCal()
green.officialCal()
green.offreap()


#green.pastclipyield()
#green.model()





print(green.pastlist)
print(green.pastacc)
print(green.forecastlist)
print(green.forecastacc)






#print(green.clipyld)


