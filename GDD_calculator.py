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
        self.day = 4

        self.apps = 1
        self.freq = 200

        self.forecastdate = []
        self.forecastlist = []
        self.forecastacc = []
        
        self.pastdate = []        
        self.pastlist = []
        self.pastacc = []
        
        self.clipyld = []

        
    def forecast (self):
        '''pulls future weather data from dark sky, and calculates daily GDDs, future and previous day. Adds to list.
        '''
        api_key = "0e7bfbdbefec8029968ab7246e77150f"
        

        lat =  32.593357 
        lng = -85.495163
        

        location = forecastio.load_forecast(api_key, lat, lng, units = "si")
            
        temphigh = []
        templow = []
        
        date = []
        day = location.daily()
    
        for i in day.data[:]:
            temphigh.append(day.data[day.data.index(i)].d['temperatureHigh'])
            templow.append(day.data[day.data.index(i)].d['temperatureLow'])
            date.append(day.data[day.data.index(i)].time)
            
        both = [temphigh] + [templow]

        self.forecastlist = [(x+y)/2 for x,y in zip(*both)]
        self.date = date
        
        return self.forecastlist



        
    def forecastCal (self):
        
        for i in range(len(self.forecastlist)):        
                   
                        
            self.forecastacc.append(sum(self.forecastlist[0:(i+1)]))
       
            
            
        return self.forecastacc     
        
    def forereap (self):
        
        for i in self.forecastacc:
            
            if  i > self.freq:
                index = self.forecastacc.index(i)
                print("reapply on: " + str(self.date[index]))
                break  
    

    def official (self):
        
        api_key = "0e7bfbdbefec8029968ab7246e77150f"
        
        
        start = datetime(2018, self.month, self.day)
        end = datetime.now()
        
        times = [start]
        
        while start < end + timedelta(days=7):
            start += timedelta(days=1)
            times.append(start)

        lat =  32.593357 
        lng = -85.495163

        temphigh = []
        templow = []
        
        for i in times:
            
            day1 = times[times.index(i)]

            location = forecastio.load_forecast(api_key, lat, lng, day1, units = "si")
                
            
            
            date = []
            day = location.daily()
        
            for i in day.data[:]:
                temphigh.append(day.data[day.data.index(i)].d['temperatureHigh'])
                templow.append(day.data[day.data.index(i)].d['temperatureLow'])
                date.append(day.data[day.data.index(i)].time)
                
        both = [temphigh] + [templow]
    
        self.pastlist = [(x+y)/2 for x,y in zip(*both)]
        self.date = date
            
        return self.pastlist

        
    def officialList(self):
        
        
        
        for i in range(len(self.pastlist)):        
                   
                        
            self.pastacc.append(sum(self.pastlist[0:(i+1)]))
       
            
            
        return self.pastacc 

    def officialCal (self):

        self.totalacc = max(self.pastacc)
       
        return self.totalacc
        
                      
                                    
                                                  
    def offreap(self):
                     








 

        return









    
    def alert (self):
            
        print("Total GDD accumulation is: " + str(self.totalacc))

        
        
        if self.totalacc > self.freq:
            print("REAPPLY!!!!")
            


#     def pastclipyield(self):
#         '''Predicts the clipping yield based on GDD
#         '''
#         for i in range(len(self.pastacc)):
#             if self.apps==1:
#                 yld = 2.42 * (2.71828 **(-self.pastacc[i]/264.1)) * math.sin((3.14159*(self.pastacc[i]+808.6))/871.7)            
#             elif self.apps>1 and self.pastacc[i] <= 300:
#                 yld = -0.60
#             elif self.apps>1 and self.pastacc[i] > 300 and self.pastacc[i] <=400:
#                 yld = -0.25
#             elif self.apps>1 and self.pastacc[i] > 400 and self.pastacc[i] <=600:
#                 yld = -0.10 
#             elif self.apps>1 and self.pastacc[i] > 600:
#                 yld = 0 
#  
#             if yld > 0:
#                 yld == 0
#                 self.clipyld.append(yld)
#             else:
#                 self.clipyld.append(yld)    
#     
#         return self.clipyld
# 
# 
#        
#     def model(self):
#         
#    
#         pylab.title('Yield Data')
#         pylab.plot(self.pastacc, self.clipyld)
#         pylab.show()



green = TEModel()
# x=0
# while x < 10:
# 
green.forecast()
green.forecastCal()
green.forereap()


#     green.official()
#     x +=1


# green.official()
# green.officialList()
# green.officialCal()
# green.alert()
#green.pastclipyield()
#green.model()




#print(green.forecastlist)
print(green.forecastacc)
# print(green.pastlist)
# print(green.pastacc)
# print(green.totalacc)
#print(green.clipyld)









