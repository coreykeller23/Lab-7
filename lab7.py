"""
Author: Corey Keller
File Name: lab7.py
Created: 3.20.24
Purpose: Process data from a csv file, perform a computation based on the data, copy data into a new csv file with new values, new header, and author footnote.
"""
#creation of key varibales and import modules
SALESAMOUNTINDEX=6
ASSESSEDVALUEINDEX=5
realEstateData=[]
import os

#begin exception handling
try:
    fileRead=open("./Labs/Real_Estate_Sales_2001-2021_GL.csv", "r")

    #process data from csv, split nad strip into a 2d array
    for row in fileRead:
        splitData = row.strip().split(",")
        realEstateData.append(splitData)
    fileRead.close()

    #create a new directory for the new csv file
    try:
        path=os.path.join(os.getcwd(), "Real Estate Prices")
        os.mkdir(path)
    except:
        pass

    #calculate values for the new column and append to the 2d array
    for row in realEstateData[1:]:
        saleDifference=float(row[SALESAMOUNTINDEX])-float(row[ASSESSEDVALUEINDEX])
        row.append(saleDifference)

    #create general function to create the new file, add new header to array, write the rows of the array into the new file, append author name and date
    def copy2dArrayWithNewColumn(array,path,fileName,header,author,date):
        fw=open(path+"/"+fileName, "w")
        headerTitle=",".join(array[0]+[header])
        fw.write(headerTitle+"\n")
        for row in array[1:]:
            row_str = ','.join(str(figure) for figure in row)
            fw.write(row_str+"\n")
        fw.close
        fa=open(fileName, "a")
        fa.write(author+":"+date)
        fa.close

    #call function with appropriate arguments
    copy2dArrayWithNewColumn(realEstateData,"Real Estate Prices","2001-2021.csv","Sales Difference","Corey Keller","3/25/2024")

#exception handling for file not found, value errors, permission errors, and unexpected errors
except FileNotFoundError:
    print("Intended file not found. Please make sure the file exists and paths are correct.")
except ValueError:
    print("Values not accepted. Please make sure the values are of the correct type.")
except PermissionError:
    print("Permission error. You do not have permission to read or edit this file")
except Exception:
    print("Unexpected error occurred. If error persists, please contact support.")