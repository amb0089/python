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
    '''Used to project clippings and GDDs based on TE application date and weather
    '''
    def __init__(self):
        
        self.year = args.year        
        self.month = args.month
        self.day = args.day
        self.freq = args.frequency

        self.forecastdate = []  #calendar date of next 15 days (not including today)
        self.forecastlist = []  #GDD for next 15 days
        self.forecastacc = []   #GDD accumulation over next 15 days
        
        self.pastdate = []      #calendar dates of application day to (including) today
        self.pastlist = []      #GDDs from appliction date to today
        self.pastacc = []       #GDD accumulation from applicaiton day to today

        self.totallistacc = []  #GDD accumulation from application day to 15 days past today
        
        self.clipyld = []       #approximate clipping suppression from application date to 15 days past today

        


    def weatherGDD (self):

        '''Pulls weather data from dark sky - from application date plus 14 days
        '''
        
        api_key = "0e7bfbdbefec8029968ab7246e77150f"
        
        
        start = datetime(self.year, self.month, self.day)
        end = datetime.now()
        
        times = [start]
        
        while start < end + timedelta(days=14):
            start += timedelta(days=1)
            times.append(start)

        #lat and long will not change by user input - future version
        lat =  32.593357 
        lng = -85.495163
    
        date = []       # a dates list without time, mm-dd-yyyy
        temphigh = []   # a list of high temps from application day to today + 15 days
        templow = []    # a list of low temps from application day to today + 15 days
        
        for i in times:
            
            day1 = times[times.index(i)]

            location = forecastio.load_forecast(api_key, lat, lng, day1, units = "si")
                  
            
            day = location.daily() # pulls daily data for each day in [times]
        
            for i in day.data[:]:
                temphigh.append(day.data[day.data.index(i)].d['temperatureHigh'])
                templow.append(day.data[day.data.index(i)].d['temperatureLow'])
                date.append(day.data[day.data.index(i)].time)
                
        
        self.totalgddlist = [(x+y)/2 for x,y in zip(temphigh, templow)] #calculates GDD for each day. ZIP creates tuple for calculation. ***BASE TEMP 0C***

        self.date = date
        
        self.pastlist = self.totalgddlist[0:-15]         # List will be empty if app date is in future, last index position is TODAY.
        self.forecastlist = self.totalgddlist[-15:]     # List will always begin with today + 1, ends with today + 15, i.e., a 15 day forecast
        self.forecastdate = self.date[-15:]             # calendar date list beginning with today + 1, ends with today + 15

                    
        return self.pastlist, self.forecastlist

        
    def pastCal(self):
        
        for i in range(len(self.pastlist)):        #checks index numbers 0 to length of pastlist + 1, i.e, for each index in pastlist sum with all previous
                         
            self.pastacc.append(sum(self.pastlist[0:(i+1)]))
     
        return self.pastacc 



    def forecastCal (self):
                
        for i in range(len(self.totalgddlist)):        #checks index numbers 0 to length of totalgddlist + 1
                             
            self.totallistacc.append(sum(self.totalgddlist[0:(i+1)]))
        
        self.forecastacc = self.totallistacc[-15:]      #list includes GDD accumulation for each future date
            
        return self.forecastacc, self.totallistacc     
        
    
    def todayGDD (self):

        if len(self.pastacc) > 0:
            self.totalgdd = max(self.pastacc)
        else:
            self.totalgdd = 0
       
        return self.totalgdd        #returns total GDD accumulation from application day to today (including)
                        
                                                  
    def reapply(self):
                     
        if self.totalgdd > self.freq:
            print("REAPPLY NOW!!!")

        
        elif self.forecastacc[-1] < self.freq:          #if frequency is not reached in forecast, then say so and give GDD accumulation on last day of forecast
                    print("Reapplication date is past forecast range (15 days). \n GDD accumulation on " + str(self.forecastdate[-1].date()) 
                            + " is expected to be " + str(int(self.forecastacc[-1])))
       
        elif len(self.pastlist) == 0:                                           
                                                        #predict date to reapply PGR, the date the GDD reapplication frequency will be obtained
            for i in self.forecastacc:          
                if i > self.freq:
                    index = self.forecastacc.index(i)
                    print("Reapply PGR on: " + str(self.forecastdate[index].date()))
                    break
        else:
            
            for i in self.forecastacc:          
                if i > self.freq:
                    index = self.forecastacc.index(i)
                    print("Reapply PGR in " + str(len(self.forecastdate[0:index])+1) + " days on: " + str(self.forecastdate[index].date()))
                    print("Current total GDD accumulation is: " + str(int(self.totalgdd)))
                    break


    def clipyield(self):
        '''Predicts the clipping yield based on GDD accumulation, cannot predict multiple applications yet
        '''
        for i in range(len(self.totallistacc)):     #uses equation from Auburn research to model clipping suppression
            
            yld = 2.42 * (2.71828 **(-self.totallistacc[i]/264.1)) * math.sin((3.14159*(self.totallistacc[i]+808.6))/871.7) 
            
            
            if yld > 0:                         #do not show growth greater than non-treated
                yld = 0
                self.clipyld.append(yld)
                            
            else:
                self.clipyld.append(yld)
                    
        return self.clipyld


        
    def model(self):    #represent clipping suppression in graphical form over dates
        
    
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
#print(green.date)


