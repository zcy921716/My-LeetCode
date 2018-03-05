"""

Design an algorithm to find all the common elements in two sorted lists of numbers.

For example, for the lists 2, 5, 5, 5 and 2, 2, 3, 5, 5, 7,
the output should be 2, 5, 5.What is themaximumnumber ofcomparisons your algorithm
makes if the lengths of the two given lists are m and n, respectively?

"""
with open('Algorithms\input.txt', 'r+') as f:
    array1 = f.readline().split()
    num_1 = [int(c) for c in array1]
    array2 = f.readline().split()
    num_2 = [int(c) for c in array2]
    point1 = 0
    point2 = 0
    common = []
    while point1 < len(num_1) and point2 < len(num_2):
        if num_1[point1] == num_2[point2]:
            common.append(str(num_1[point1]))
            point1 += 1
            point2 += 1
        elif num_1[point1] > num_2[point2]:
            point2 += 1
        else:
            point1 += 1
    f.write(' '.join(common))
