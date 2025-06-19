import csv
import matplotlib.pyplot as plt
import numpy as np


# easily read a .txt file into a list of numbers
def easyRead(fileName):
  fileIn = open(fileName,"r")

 
  
  lstTemStrings = fileIn.read().splitlines()

  # for loop to make the strings into numbers
  lstTemNumbers = [float(item) for item in lstTemStrings]
 
  # returns the cleaned up list
  return lstTemNumbers

# generates a list of nums from 1 to the given value, inclusive
def rangeList(nums):
  return list(range(1,nums + 1))

# uses two lists to create a simple linegraph
def lineGraph(xNums, yNums):

  #checks that x values and y values are the same length
  if(len(xNums) == len(yNums)):
    plt.plot(xNums, yNums)
    plt.show()
  else:
    print("The lists must be the same length")

# creates a simple bar graph
def barGraph(categories, values):
  #checks that x values and y values are the same length
  if(len(categories) == len(values)):
    plt.bar(categories, values)
    plt.show()
  else:
    print("The lists must be the same length") 

# simple scatter plot
def scatterPlot(xNums, yNums):
  #checks that x values and y values are the same length
  if(len(xNums) == len(yNums)):
    plt.scatter(xNums, yNums)
    plt.show()
  else:
    print("The lists must be the same length")

# Simple pie chart
def simplePie(cats, labels):
  if(len(cats) == len(labels)):
    plt.pie(cats, labels = labels)
    plt.show()
  else:
    print("Number of categories and number of proportions must match")


# method takes a file name and the desired column (starting at 0)
# then returns it as a list of Strings
def colToList(fileName, colNum):
  # creates empty list and label to prep for return
  lst = []
  label = ""

  #opens given file
  with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0

    # uses for loop to get each line
    # the first value per line is saved as a label
    for row in csv_reader:
      lst.append(row[colNum])
      lineNum += 1

  # uses Python's multiple return feature to return both
  # the label and the actual list of information
  return lst
      
    
# method takes a file name and the desired column (starting at 0)
# then returns it as a list of floats (decimal numbers)
def colToListNumbers(fileName, colNum):
  # creates empty list and label to prep for return
  lst = []
  label = ""

  #opens given file
  with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0

    # uses for loop to get each line
    # the first value per line is saved as a label
    for row in csv_reader:
      lst.append(float(row[colNum]))
      lineNum += 1

  # uses Python's multiple return feature to return both
  # the label and the actual list of information
  return lst


