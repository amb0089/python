import pylab, math
import forecastio
from datetime import datetime, timedelta
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-d', '--day', help="Enter the app date with no spaces", type = int)

parser.add_argument('-m', '--month', help="Enter the app month (number) with no spaces", type = int)

parser.add_argument('-y', '--year', help="Enter the app year with no spaces", type = int)

parser.add_argument('-f', '--frequency', help="Enter the app frequency with no spaces", type = int)

args = parser.parse_args()



class TEModel(object):
    '''Used to project clippings based on TE apps and weather
    '''
    def __init__(self):
        
        self.year = args.year        
        self.month = args.month
        self.day = args.day
        self.freq = args.frequency

        self.forecastdate = []
        self.forecastlist = []
        self.forecastacc = []
        
        self.pastdate = []        
        self.pastlist = []
        self.pastacc = []

        self.totallistacc = []
        
        self.clipyld = []

        


    def weatherGDD (self):
        
        api_key = "0e7bfbdbefec8029968ab7246e77150f"
        
        
        start = datetime(self.year, self.month, self.day)
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
    
        self.totalgddlist = [(x+y)/2 for x,y in zip(*both)]
        self.date = date

        self.pastlist = self.totalgddlist[0:-15]
        self.forecastlist = self.totalgddlist[-15:]
        self.forecastdate = self.date[-15:]
            
        return self.pastlist, self.forecastlist

        
    def pastCal(self):
        
        for i in range(len(self.pastlist)):        
                         
            self.pastacc.append(sum(self.pastlist[0:(i+1)]))
     
        return self.pastacc 



    def forecastCal (self):
                
        for i in range(len(self.totalgddlist)):        
                             
            self.totallistacc.append(sum(self.totalgddlist[0:(i+1)]))
        
        self.forecastacc = self.totallistacc[-15:]
            
        return self.forecastacc, self.totallistacc     
        
    
    def todayGDD (self):

        if len(self.pastacc) > 0:
            self.totalgdd = max(self.pastacc)
        else:
            self.totalgdd = 0
       
        return self.totalgdd
                        
                                                  
    def reapply(self):
                     
        if self.totalgdd > self.freq:
            print("REAPPLY NOW!!!")

        elif self.forecastacc[-1] < self.freq:
                    print("Reapplication date is past forecast range (14 days). \n GDD accumulation on " + str(self.forecastdate[-1].date()) 
                            + " is expected to be " + str(int(self.forecastacc[-1])))
        else:
            for i in self.forecastacc:          
                if i > self.freq:
                    index = self.forecastacc.index(i)
                    print("Reapply PGR on: " + str(self.forecastdate[index].date()))
                    if len(self.pastacc)> 0: 
                        print("Current total GDD accumulation is: " + str(int(self.totalgdd)))
                        break
                    else:
                        break
                    

    def clipyield(self):
        '''Predicts the clipping yield based on GDD
        '''
        for i in range(len(self.totallistacc)):
            
            yld = 2.42 * (2.71828 **(-self.totallistacc[i]/264.1)) * math.sin((3.14159*(self.totallistacc[i]+808.6))/871.7) 
            
            
            if yld > 0:
                yld = 0
                self.clipyld.append(yld)
                            
            else:
                self.clipyld.append(yld)
                    
        return self.clipyld


        
    def model(self):
        
    
        pylab.title('Yield Data')
        pylab.xlabel('Date')
        pylab.ylabel('Clipping Yield Relative Difference')
        pylab.plot(self.date, self.clipyld)
        pylab.show()





if __name__ == "__main__":
          
    green = TEModel()
    green.weatherGDD()
    
    green.pastCal()
    green.forecastCal()
    
    green.todayGDD()
    green.reapply()
    
    
    green.clipyield()
    green.model()





#print(green.pastlist)
# print(green.pastacc)
#print(green.forecastlist)
# print(green.forecastacc)
# print(green.clipyld)


