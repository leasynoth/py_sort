# -*- coding: utf-8 -*-

__author__ = 'leasynoth'
__email__ = 'nordiccastinc@gmail.com'
__DATE__ = '29.01.2019'

'''

    Coctail sort

'''

import random as rand
import time


defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323] 

def coctailSort(data=defaultData, way=0): 
    
    startTime = time.time()
    
    count = 0
    
    iMin = count
    iMax = len(data)-1
    
    if (way == 0):
        
        while (iMin <= iMax):
            
            if (count % 2 == 0):
                
                for i in range(iMin, iMax):
                    
                    if data[i] < data[i+1]:
                        
                        data[i], data[i+1] = data[i+1], data[i]
                        
                iMax -= 1
                
            elif (count % 2 != 0):
                
                for i in range(iMax, iMin, -1):
                    
                    if data[i] > data[i-1]:
                        
                        data[i], data[i-1] = data[i-1], data[i]
                
                iMin += 1
            
            count += 1
            
    elif(way == 1):
        
         while(iMin <= iMax):
             
            if (count % 2 == 0):
                 
                for i in range(iMin, iMax):
                    
                    if (data[i] > data[i+1]):
                        
                        data[i], data[i+1] = data[i+1], data[i]
                        
                iMax -= 1         
                 
            elif (count % 2 != 0):
                
                for i in range(iMax, iMin, -1):
                    
                    if (data[i] < data[i-1]):
                        
                        data[i], data[i-1] = data[i-1], data[i]
                        
                iMin += 1            
        
            count += 1
    
    else:
        
        print('The second argument indicates the sort order: 0 - in descending order, 1 - in ascending order.')        
            
    endTime = time.time()
    
    print('Lead time: {:.3f} s.'.format(endTime - startTime))
        
    return data
    
    
    
def main():
    
    # uncomment output for visualization 
    
    randData = list(range(rand.randint(9000, 9000)))
    rand.shuffle(randData) 
    
    #print('Default data: \n' + str(randData) + '\n')
    
    descend = coctailSort(randData, 0)

    #print('Coctail sorting in descending order: \n' + str(descend))
    
    rand.shuffle(randData)
    
    #print('Default data: \n' + str(randData) + '\n')
    
    ascend = coctailSort(randData, 1)
    
    #print('Coctail sorting in ascending order: \n' + str(ascend))
    
    
if __name__ == '__main__':
    
    main()            