import numpy as np
import math
import os
os.getcwd()


def bbox2Cpoint(list1):
    # this function get the center point of bounding box
    cpoint = []
    x1 = (list1[0] + list1[2]) / 2
    y1 = (list1[1] + list1[3]) / 2
    cpoint.append(x1)
    cpoint.append(y1)
    return cpoint

def disPoint(cpoint1, cpoint2):
    #this function caculate the distance of two point
    distance = math.sqrt((cpoint1[0] - cpoint2[0]) ** 2 + (cpoint1[1] - cpoint2[1]) ** 2)
    return distance

def disArray(frame1, frame2):
    #this function caculate the two frame distance
    dim_x = len(frame1)
    dim_y = len(frame2)
    #init the array of the ditance
    arrayDistace = np.zeros((dim_x, dim_y))
    for i in range(dim_x):
        for j in range(dim_y):
            arrayDistace[i][j] = disPoint(frame1[i], frame2[j])
    return arrayDistace

def minIndex(arrayDistance):
    #this function get the min number index
    #the first number is Row
    #the second number is Colum
    minNum = arrayDistance.min()
    a, b = np.where(arrayDistance == minNum)
    return a, b

def newArraydis(arrayDistance, a, b):
    #this function delete the Row a and the Colum b
    m, n = arrayDistance.shape
    for i in range(n):
        arrayDistance[int(a)][i] += 1000
    for i in range(m):
        arrayDistance[i][int(b)] += 1000
    return arrayDistance

if __name__ =="__main__":
    print("please input the total frame")
    result = []
    num = input()
    num = int(num)
    frameBbox = np.loadtxt('output/00000%d.txt' % 1)
    framePoint = []
    for j in range(len(frameBbox)):
        point = []
        point = bbox2Cpoint(frameBbox[j])
        framePoint.append(point)
    for i in range(1, num):
        frame1Point = framePoint
        if i < 9:
            frame2Bbox = np.loadtxt('output/00000%d.txt' % (i + 1))
        else:
            frame2Bbox = np.loadtxt('output/0000%d.txt' %(i + 1))
        frame2Point = []
        #get the point from each frame
        for j in range(len(frame2Bbox)):
            point = []
            point = bbox2Cpoint(frame2Bbox[j])
            frame2Point.append(point)
        distanceList = disArray(frame1Point, frame2Point)
        indexArray = []
        minNum = min(distanceList.shape)
        for i in range(minNum):
            a, b = minIndex(distanceList)
            temp = []
            temp.append(a)
            temp.append(b)
            if distanceList[int(a)][int(b)] < 20:
                indexArray.append(temp)
            else:
                temp[1] = -1
                indexArray.append(temp)
            distanceList = newArraydis(distanceList, a, b)
        result.append(indexArray)
        framePoint = frame2Point
    print(result[1])
