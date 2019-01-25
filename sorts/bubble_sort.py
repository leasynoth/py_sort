# -*- coding: utf-8 -*-

# bubble sort

__author__ = 'vanzann'
__email__ = 'nordiccatinc@gmail.com'
__DATE__ = '24.01.2019'


defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323]

def bubbleSort(data=defaultData, way=0):
    

    if (way == 0): # in descending order
        
        count = 1
        
        while (count <= len(data)-1):
            
            for index in range(len(data)-count):
                
                if data[index] < data[index+1]:
                    
                    data[index], data[index+1] = data[index+1], data[index]
                    
            count += 1
        
    elif(way == 1): # in ascending order
        
        count = 1
        
        while (count <= len(data)-1):
            
            for index in range(len(data)-count):
                
                if data[index] > data[index+1]:
                    
                    data[index], data[index+1] = data[index+1], data[index]
            
            count += 1
        
    else:
        
        print('The second argument indicates the sort order: 0 - in descending order, 1 - in ascending order.')        
    
    return data
        
        
def main():
    
    defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323] 
    
    print('Default data: ' + str(defaultData) + '\n')
    
    descend = bubbleSort(defaultData, 0)
    
    print('Bubble sorting in descending order: ' + str(descend))
    
    ascend = bubbleSort(defaultData, 1)
    
    print('Bubble sorting in ascending order: ' + str(ascend))
    

        
if __name__ == '__main__':
    
    main()        