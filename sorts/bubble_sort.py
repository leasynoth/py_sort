# -*- coding: utf-8 -*-

__author__ = 'leasynoth'
__email__ = 'nordiccatsinc@gmail.com'
__DATE__ = '24.01.2019'

'''

    Bubble sort

'''

import random as rand
import time


defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323]

def bubbleSort(data=defaultData, way=0):
    
    startTime = time.time()
    
    if (way == 0): # in descending order
        
        count = 1
        
        while (count <= len(data)-1):
            
            for index in range(len(data)-count):
                
                if data[index] < data[index+1]:
                    
                    data[index], data[index+1] = data[index+1], data[index]
                    
            count += 1
        
    elif (way == 1): # in ascending order
        
        count = 1
        
        while (count <= len(data)-1):
            
            for index in range(len(data)-count):
                
                if data[index] > data[index+1]:
                    
                    data[index], data[index+1] = data[index+1], data[index]
            
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
    
    descend = bubbleSort(randData, 0)
    
    #print('Bubble sorting in descending order: \n' + str(descend))
    
    rand.shuffle(randData)
    
    #print('Default data: \n' + str(randData) + '\n')
    
    ascend = bubbleSort(randData, 1)
    
    #print('Bubble sorting in ascending order: \n' + str(ascend))
    

if __name__ == '__main__':
    
    main()        