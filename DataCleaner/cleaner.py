import sys
import re
import time



file = open("C:/Users/mario/Desktop/TrainingData/test/educational/educationTest.txt",'r',encoding='utf-8')
i = 1
for line in file.readlines():
    newFile = open('C:/Users/mario/Desktop/TrainingData/test/educational/'+str(i)+'.txt','w',encoding='utf-8')
    #Get only ascii values
    filterOne = " ".join(re.findall('[\x00-\x7F]+',line))
    #get only alphanumeric values
    filterTwo = " ".join(re.findall('\w+',filterOne))
    #filter out the numbers
    filterThree = " ".join(re.findall('\D+',filterTwo))
    newFile.write(filterThree)
    newFile.close()
    i+=1
    if i == 10000:
        print("50% Done!")


file.close()
print("100% Done!")
#create file
#clean title
#save
# repeat
