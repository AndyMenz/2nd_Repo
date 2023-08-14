import time
def count_down():
    sec=int(input('Enter your number: '))
    while sec:
         mins,secs = divmod(sec,60)
         timeformat = '{:02d} : {:02d}:{:02d}'.format(mins,secs)
         print (timeformat)
         time.sleep(1)
         sec-=1
          
        
count_down()



