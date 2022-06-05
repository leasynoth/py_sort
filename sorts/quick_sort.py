# -*- coding: utf-8 -*-

__author__ = 'leasynoth'
__email__ = 'nordiccatsinc@gmail.com'
__DATE__ = '28.04.2022'


'''

    Quick sort

'''


import random as rand
import time


defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323]

def quickSort(data=defaultData, way=0):

    if (way == 0):

        if (len(data) < 2):

            return data

        support = data[len(data)-1]
        leftArr = []
        rightArr = []
        centerArr = []

        for elem in data:

            if (support > elem):

                leftArr.append(elem)

            elif (support < elem):

                rightArr.append(elem)

            elif (support == elem):

                centerArr.append(elem)

        return quickSort(leftArr, way) + quickSort(centerArr, way) + quickSort(rightArr, way)

    elif (way == 1):

        if (len(data) < 2):

            return data

        support = data[len(data)-1]
        leftArr = []
        rightArr = []
        centerArr = []

        for elem in data:

            if (support < elem):

                leftArr.append(elem)

            elif (support > elem):

                rightArr.append(elem)

            elif (support == elem):

                centerArr.append(elem)

        return quickSort(leftArr, way) + quickSort(centerArr, way) + quickSort(rightArr, way)


def main():

    # uncomment output for visualization

    randData = list(range(rand.randint(9000, 9000)))
    rand.shuffle(randData)

    #print('Default data: \n' + str(randData) + '\n')

    startTime = time.time()
    descend = quickSort(randData, 0)
    endTime = time.time()

    print('Lead time (descend order): {:.3f} s.'.format(endTime - startTime))
    #print('Quick sorting in descending order: \n' + str(descend))

    rand.shuffle(randData)

    #print('Default data: \n' + str(randData) + '\n')

    startTime = time.time()
    ascend = quickSort(randData, 1)
    endTime = time.time()

    print('Lead time (ascend order): {:.3f} s.'.format(endTime - startTime))
    # print('Quick sorting in ascending order: \n' + str(ascend))


if __name__ == '__main__':

    main()
