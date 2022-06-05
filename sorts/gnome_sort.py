# -*- coding: utf-8 -*-

__author__ = 'leasynoth'
__email__ = 'nordiccatsinc@gmail.com'
__DATE__ = '15.04.2022'

'''

    Gnome sort

'''

import random as rand
import time


defaultData = [12, 3123234, 234, 2341, 334344, 14421212, 324345, 4, 12323]

def gnomeSort(data=defaultData, way=0):

    startTime = time.time()

    if (way == 0):

        count = 1

        while (count <= len(data)-1):

            if (data[count-1] > data[count]):

                data[count-1], data[count] = data[count], data[count-1]

                if (count > 1):

                    count -= 1
            else:

                count += 1

    elif (way == 1):

        count = 1

        while (count <= len(data)-1):

            if (data[count-1] < data[count]):

                data[count-1], data[count] = data[count], data[count-1]

                if (count > 1):

                    count -= 1
            else:

                count += 1


    endTime = time.time()

    print('Lead time: {:.3f} s.'.format(endTime - startTime))

    return data


def main():

    # uncomment output for visualization

    randData = list(range(rand.randint(9000, 9000)))
    rand.shuffle(randData)

    #print('Default data: \n' + str(randData) + '\n')

    descend = gnomeSort(randData, 0)
    #descend = gnomeSort(way=0)

    print('Gnome sorting in descending order: \n' + str(descend))

    rand.shuffle(randData)

    #print('Default data: \n' + str(randData) + '\n')

    ascend = gnomeSort(randData, 1)
    #ascend = gnomeSort(way=1)

    #print('Gnome sorting in ascending order: \n' + str(ascend))


if __name__ == '__main__':

    main()