# -*-coding: utf-8 -*-

# coctail sort

__author__ = 'leasynoth'
__email__ = 'nordiccatinc@gmail.com'
__DATE__ = '29.01.2019'

#defaultData = [232, 57, 3, 36, 123, 2356, 0, 123, 4595, 12356, 45, 985]
defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323] 

def coctailSort(data=defaultData, way=0): 
    
    count = 0
    
    iMin = count
    iMax = len(data)-1
    
    while (iMin <= iMax):
        
        if (count % 2 == 0):
            
            for i in range(iMin, iMax):
                
                if data[i] > data[i+1]:
                    
                    data[i], data[i+1] = data[i+1], data[i]
                    
            iMax -= 1
            
        elif (count % 2 != 0):
            
            for i in range(iMax, iMin, -1):
                
                if data[i] < data[i-1]:
                    
                    data[i], data[i-1] = data[i-1], data[i]
            
            iMin += 1
        
        count += 1
        
        
    return data
    
    
    
def main():
    
    #defaultData = [232, 57, 3, 36, 123, 2356, 0, 123, 4595, 12356, 45, 985]
    
    defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323] 
    
    print('Default data: ' + str(defaultData) + '\n')
    
    test = coctailSort(defaultData, 0)
    
    print('Coctail sorting: ' + str(test))
    
    
if __name__ == '__main__':
    
    main()            