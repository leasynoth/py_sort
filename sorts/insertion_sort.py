# -*- coding: utf-8 -*-

# Insertion sorting

import time
import random as rand


defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323]

def insertionSort(data=defaultData, way=0):
    
    startTime = time.time()
    
    count = 0
    resArr = []
    dataLenght = len(data)-1
    
    if (way == 0):
        
        while (count <= dataLenght):
            
            if (len(resArr) == 0):
                
                resArr.append(data.pop(0))
                
                count += 1
                
                continue
                
                
            else:
                
                for i in range(len(resArr)):
                    
                    if (resArr[i] < data[0]):
                        
                        if (i == len(resArr)-1):
                            
                            resArr.append(data.pop(0))
                            
                            count += 1
                        
                            break
                        
                    elif (resArr[i] > data[0]):
                        
                        resArr.insert(i, data.pop(0))
                        
                        count += 1
                        
                        break
                        
                    else:
                        
                        resArr.insert(i+1, data.pop(0))
                        
                        count += 1
                        
                        break
            
    elif (way == 1):
        
        while (count <= dataLenght):
            
            if (len(resArr) == 0):
                
                resArr.append(data.pop(0))
                
                count += 1
                
                continue
                
                
            else:
                
                for i in range(len(resArr)):
                    
                    if (resArr[i] > data[0]):
                        
                        if (i == len(resArr)-1):
                            
                            resArr.append(data.pop(0))
                            
                            count += 1
                        
                            break
                        
                    elif (resArr[i] < data[0]):
                        
                        resArr.insert(i, data.pop(0))
                        
                        count += 1
                        
                        break
                        
                    else:
                        
                        resArr.insert(i+1, data.pop(0))
                        
                        count += 1
                        
                        break
        
    else: 
    
        print('The second argument indicates the sort order: 0 - in descending order, 1 - in ascending order.')        
        
    endTime = time.time()
    
    print('Lead time: {:.3f} s.'.format(endTime - startTime))
    
    return resArr
    
    
def main():
    
    # uncomment output for visualization 
    
    randData = list(range(rand.randint(9000, 9000)))
    rand.shuffle(randData) 
    
    #print('Default data: \n' + str(randData) + '\n')
    
    descend = insertionSort(randData, 0)
    
    #print('Insertion sorting in descending order: \n' + str(descend))
    
    randData = list(range(rand.randint(9000, 9000)))
    rand.shuffle(randData)
    
    #print('Default data: \n' + str(randData) + '\n')

    ascend = insertionSort(randData, 1)
    
    #print('Insertion sorting in ascending order: \n' + str(ascend))
    
    
if __name__ == '__main__':
    
    main()
    
    
    
    