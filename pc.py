import pandas as pd
from numpy import *
import numpy as np


data =pd.read_csv('train.csv')
array = data.values

dimension = len(array[0])
print("Dimension of the data points is : ",dimension)
print("\n")

covarianceMatrix = np.cov(array,rowvar=False)
meanOfColumns = np.mean(array,axis=0)

print("Means are: ")
print(meanOfColumns)
print("\n")

print("Enter one for finding the Mahalanobis distance between two points and 2 for finding the Mahalanobis distance for a point\n")

choice = input();

if choice ==1:
	x=list()
	y=list()
	print("Enter the input points x\n")
	for i in range(dimension):
		temp =input()
		x.append(temp)
	print("Enter the input points x\n")
	for i in range(dimension):
		temp =input()
		y.append(temp)
	MahalanobisDistance = sqrt(np.matmul(np.matmul(np.subtract(x,y),np.linalg.inv(covarianceMatrix)),np.subtract(x,y)))
	print("Mahalanobis Distance between given points is ",MahalanobisDistance)
	
else:
	x=list()
	print("Enter the input point x\n")
	for i in range(dimension):
		temp =input()
		x.append(temp)
	MahalanobisDistance = sqrt(np.matmul(np.matmul(np.subtract(x,meanOfColumns),np.linalg.inv(covarianceMatrix)),np.subtract(x,meanOfColumns)))
	print("Mahalanobis Distance between given points is ",MahalanobisDistance)
		


	
	
	
	




